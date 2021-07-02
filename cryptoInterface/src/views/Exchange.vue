<template>
  <div>
    <v-tabs background-color="background" center-active centered>
      <v-tab @click="getPairs('Spot', slug)">Spot</v-tab>
      <v-tab @click="getPairs('Perpetual', slug)">Perpetual</v-tab>
      <v-tab @click="getPairs('Futures', slug)">Futures</v-tab>
    </v-tabs>

    <v-data-table
      class="transparent"
      :headers="headers1"
      :items="items1"
      :page="page"
      :pageCount="numberOfPages"
      :options.sync="options"
      :server-items-length="totalItems"
      :loading="loading"
      sort-by="name"
      @onclick="cenas()"
    >
      <!-- <template v-slot:item.id="{ item }">
            <div class="p-2">
              <v-img 
                :src="'https://s2.coinmarketcap.com/static/img/coins/64x64/' + item.id + '.png'" 
                :alt="item.name" 
                height="50px"
                max-width="50px"
              >
              </v-img>
            </div>
          </template> -->

      <template v-slot:item.exchange="{ item }">
        <a :href="`/exchange/${item.prices.exchangeSlug}`">
          {{ item.prices.exchangeName }}
        </a>
      </template>

      <template v-slot:item.pairs="{ item }">
        <!-- <a :href="`/coin/${item.slug}`"> {{ item.name }} ( {{ item.symbol }} ) -->
        <a :href="`/coin/${item.slugBuy}`"> {{ item.namebuy }} </a>
        <a :href="`${item.marketurl}`"> ( {{ item.prices.marketPair }} ) </a>
        <a :href="`/coin/${item.slugSell}`"> {{ item.namesell }} </a>

        <!-- <span
          >{{item.prices.baseSymbol}}/{{item.prices.quoteSymbol}}</span
        > -->
      </template>

      <template v-slot:item.prices="{ item }">
        <span>
          $ {{ parseFloat(item.prices.price.toFixed(2)).toLocaleString() }}
        </span>
      </template>

      <template v-slot:item.depthpositive="{ item }">
        <td v-if="item.prices.depthUsdPositiveTwo">
          ${{
            parseFloat(
              item.prices.depthUsdPositiveTwo.toFixed(0)
            ).toLocaleString()
          }}
        </td>
        <td v-else>-</td>
        <!-- <span
          >{{
            parseFloat(
              item.prices.depthUsdPositiveTwo.toFixed(0)
            ).toLocaleString()
          }}
          %</span> -->
      </template>

      <template v-slot:item.depthnegative="{ item }">
        <td v-if="item.prices.depthUsdNegativeTwo">
          ${{
            parseFloat(
              item.prices.depthUsdNegativeTwo.toFixed(0)
            ).toLocaleString()
          }}
        </td>
        <td v-else>-</td>
      </template>

      <template v-slot:item.volume="{ item }">
        <span
          >${{ parseFloat(item.prices.volumeUsd.toFixed(0)).toLocaleString() }}
        </span>
      </template>
      <template v-slot:item.volumeperc="{ item }">
        <span
          >{{
            parseFloat(item.prices.volumeUsd.toFixed(0)).toLocaleString()
          }}
          %</span
        >
      </template>
      <template v-slot:item.liquidity="{ item }">
        <span>{{
          parseFloat(item.prices.effectiveLiquidity.toFixed(2)).toLocaleString()
        }}</span>
      </template>

      <template v-slot:item.lastupdate="{ item }">
        <span> {{ item.prices.lastUpdated }}</span>
      </template>
    </v-data-table>

    <div>
      <p>{{ item.about }}</p>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "Exchange",
  data: () => {
    return {
      item: {},
      // categories: [],
      // algorithms: [],
      // industries: [],
      // plataform: [],
      explorers: [],
      prices: {},
      tradingPairs: [],
      page: 1,
      totalItems: 0,
      numberOfPages: 0,
      loading: true,
      options: {},
      headers1: [
        {
          text: "Source",
          value: "id",
          align: "start",
          sortable: false,
        },
        {
          text: "Exchange",
          value: "exchange",
          align: "start",
        },
        {
          text: "Pairs",
          value: "pairs",
          align: "center",
        },
        {
          text: "Price",
          value: "prices",
          align: "end",
        },
        {
          text: "+2% Depth",
          value: "depthpositive",
          align: "end",
        },
        {
          text: "-2% Depth",
          value: "depthnegative",
          align: "end",
        },
        {
          text: "Volume",
          value: "volume",
          align: "end",
        },
        {
          text: "Liquidity%",
          value: "liquidity",
          align: "end",
        },
        {
          text: "Last Update",
          value: "lastupdate",
          align: "end",
        },
        // {
        //   text: "Volume (24h)",
        //   value: "volume_24h",
        //   align: "end",
        // },
        // {
        //   text: "Circulation Supply",
        //   value: "circ_supply",
        //   align: "end",
        // },
      ],
      items1: [],
      slug: "",
    };
  },

  watch: {
    options: {
      handler() {
        this.readData();
      },
    },
    deep: true,
  },

  created() {
    this.buscarExchange();
    //this.readData();
  },

  // mounted(){
  //     this.readData();
  // },

  methods: {
    // redirect: function (link, target = '_blank') {
    //   console.log('target', target)
    //   window.open(link, target);
    // },

    buscarExchange() {
      let url = window.location.href;
      let exchange_slug = url.split("/").slice(-1).pop();
      this.$request("get", `exchanges/${exchange_slug}`)
        .then((data) => {
          console.log("data-total", data);
          //console.log('data.data[0]', data.data[0])
          // data.map(e => {
          //   console.log('e', e)
          // })
          //console.log(data.data[0])
          this.item = data.data[0];
          // this.categories = data.data[0].nomecat
          // this.algorithms = data.data[0].nomeal
          // this.industries = data.data[0].nomeind
          // this.plataform = data.data[0].nomeplat
          // console.log('tags', this.categories)
          this.slug = data.data[0].slug;
        })
        .catch((e) => console.log(e));
    },

    getPairs(type, exchange_slug) {
      console.log("getPairs");

      this.loading = true;
      const { page, itemsPerPage } = this.options;
      let pageNumber = page - 1;

      pageNumber = pageNumber === -1 ? 0 : pageNumber;
      //console.log('pag number', pageNumber)
      //console.log('slug', coin_slug)

      let url =
        "tradingPairs/exchange/" +
        exchange_slug +
        "/type/" +
        type +
        "Pair?size=" +
        itemsPerPage +
        "&page=" +
        pageNumber;
      console.log("url", url);

      this.$request("get", url)
        .then((data) => {
          console.log("data -> ", data);
          //this.items1 = data.data.dados;
          this.totalItems = data.data.totalItems;
          this.numberOfPages = data.data.numberOfPages;
          //console.log('total items', data.data.totalItems, 'number of pages', data.data.numberOfPages)

          let ids = data.data.dados.map((e) => e.marketid).toString();
          //console.log('ids', ids);
          this.getPrices(
            ids,
            data.data.dados,
            exchange_slug,
            type.toLowerCase()
          );
        })
        .catch((e) => console.log(e));
    },

    readData() {
      console.log("readData");
      console.log("options", this.options);
      let myurl = window.location.href;

      let exchange_slug = myurl.split("/").slice(-1).pop();
      this.loading = true;
      const { page, itemsPerPage } = this.options;
      let pageNumber = page - 1;
      pageNumber = pageNumber === -1 ? 0 : pageNumber;

      let url =
        "tradingPairs/exchange/" +
        exchange_slug +
        "/type/SpotPair?size=" +
        itemsPerPage +
        "&page=" +
        pageNumber;
      console.log("readData url", url);
      this.$request("get", url)
        .then((data) => {
          console.log("data -> ", data);
          //this.items1 = data.data.dados;
          this.totalItems = data.data.totalItems;
          this.numberOfPages = data.data.numberOfPages;
          //console.log('total items', data.data.totalItems, 'number of pages', data.data.numberOfPages)

          let ids = data.data.dados.map((e) => e.marketid).toString();
          //console.log('ids', ids);
          this.getPrices(ids, data.data.dados, exchange_slug, "spot");
        })
        .catch((e) => console.log(e));
    },

    getPrices(ids, dados, slug, type) {
      let url = `marketPairPriceExchange?slug=${slug}&category=${type}&market=${ids}`;
      console.log("getPrices url", url);
      this.$request(
        "getp",
        `marketPairPriceExchange?slug=${slug}&category=${type}&market=${ids}`
      )
        .then((data) => {
          //console.log(data.data);
          let prices = Object.values(data.data).map((item) => {
            return item;
          });

          console.log("prices", prices);
          this.items1 = dados;
          prices.map((e, index) => {
            this.items1[index]["prices"] = e;
            //this.items1[index]["circ_supply"] = Object.values(data.data)[index]["circulating_supply"];
          });
          this.loading = false;
          console.log("items1", this.items1);
        })
        .catch((e) => console.log(e));
    },
  },

  computed: {
    ...mapGetters(["carts"]),
  },
};
</script>
