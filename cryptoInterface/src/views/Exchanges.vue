<template>
  <div>
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
      <template v-slot:item.id="{ item }">
            <div class="p-2">
              <v-img 
                :src="'https://s2.coinmarketcap.com/static/img/exchanges/64x64/' + item.id + '.png'" 
                :alt="item.name" 
                height="50px"
                max-width="50px"
              >
              </v-img>
            </div>
          </template>
      <template v-slot:item.name="{ item }">
        <a :href="`/exchange/${item.slug}`"> {{ item.name }}
          
        </a>
      </template>
      <template v-slot:item.score="{ item }">
        <span 
          >{{item.exchange_score}}
        </span>
      </template>

      <template v-slot:item.volume_24h="{ item }">
        <span
          >$ {{
            parseFloat(
              item.prices.volume_24h.toFixed(2)
            ).toLocaleString()
          }}
          </span
        >
      </template>
      <template v-slot:item.visits="{ item }">
        <span
          >{{item.visits}}</span
        >
      </template>

      <template v-slot:item.num_market_pairs="{ item }">
        <span>{{item.num_market_pairs}}</span>
      </template>

      <template v-slot:item.num_coins="{ item }">
        <span
          >{{item.num_coins}}
        </span>
      </template>
      
    </v-data-table>
    <v-btn href="coin/1">Ola</v-btn>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "Home",
  data: () => {
    return {
      itemid: 0,
      page: 1,
      totalItems: 0,
      numberOfPages: 0,
      loading: true,
      options: {
      },

      headers1: [
        {
          text: "Logo",
          value: "id",
          align: "start",
          sortable: false,
        },
        {
          text: "Name",
          value: "name",
          align: "start",
        },
        {
          text: "Exchange Score",
          value: "score",
          align: "end",
        },
        {
          text: "Volume (24h)",
          value: "volume_24h",
          align: "end",
        },
        {
          text: "Weekly Visits",
          value: "visits",
          align: "end",
        },
        {
          text: "# Markets",
          value: "num_market_pairs",
          align: "end",
        },
        {
          text: "# Coins",
          value: "num_coins",
          align: "end",
        },

      ],
      items1: [],
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
    //this.readData();
    //console.log("final", this.items1);
  },
  methods: {
    readData() {
      let url = window.location.href
      let exchange_type = url.split("/").slice(-1).pop()

      this.loading = true;
      const { page, itemsPerPage } = this.options;
      let pageNumber = page - 1;
      pageNumber = pageNumber === -1 ? 0 : pageNumber;
      console.log('pag number', pageNumber)
      let url_req = 'exchanges/type/' + exchange_type + '?size=' + itemsPerPage + '&page=' + pageNumber
      this.$request("get", url_req)
        .then((data) => {
          console.log('exchanges -> ', data)
          //this.items1 = data.data.dados;
          this.totalItems = data.data.totalItems;
          this.numberOfPages = data.data.numberOfPages;
          //console.log('total items', data.data.totalItems, 'number of pages', data.data.numberOfPages)
          
          let ids = data.data.dados.map((e) => e.id).toString();

          this.getPrices(ids, data.data.dados);
        })
        .catch((e) => console.log(e));

    },

    getPrices(ids, dados) {
      this.$request("getp", `exchangePrice?id=${ids}`)
        .then((data) => {
          //console.log(data.data);
          let prices = Object.values(data.data).map((item) => {
            return item.quote.USD;
          });
          this.items1 = dados;
          prices.map((e, index) => {
            this.items1[index]["prices"] = e;
            this.items1[index]["exchange_score"] = Object.values(data.data)[index]["exchange_score"];
            this.items1[index]["last_updated"] = Object.values(data.data)[index]["last_updated"];
            this.items1[index]["num_coins"] = Object.values(data.data)[index]["num_coins"];
            this.items1[index]["num_market_pairs"] = Object.values(data.data)[index]["num_market_pairs"];
            this.items1[index]["traffic_score"] = Object.values(data.data)[index]["traffic_score"];
            this.items1[index]["visits"] = Object.values(data.data)[index]["visits"];

          })

          console.log('items final', this.items1)
          this.loading = false;
        })
        .catch((e) => console.log(e));
    },
  },
  computed: {
    ...mapGetters(["carts"]),
  },
};
</script>
