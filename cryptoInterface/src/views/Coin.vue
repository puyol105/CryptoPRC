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
        <span> {{ item.prices.exchangeName }}
          
        </span>
      </template>
      <!-- <template v-slot:item.pricesP="{ item }">
        <span
          >$
          {{ parseFloat(item.prices.price.toFixed(2)).toLocaleString() }}</span
        >
      </template>
      <template v-slot:item.prices24="{ item }">
        <span
          >{{
            parseFloat(
              item.prices.percent_change_24h.toFixed(2)
            ).toLocaleString()
          }}
          %</span
        >
      </template>
      <template v-slot:item.prices7="{ item }">
        <span
          >{{
            parseFloat(
              item.prices.percent_change_7d.toFixed(2)
            ).toLocaleString()
          }}
          %</span
        >
      </template>
      <template v-slot:item.marketCap="{ item }">
        <span>{{
          parseFloat(item.prices.market_cap.toFixed(2)).toLocaleString()
        }}</span>
      </template>
      <template v-slot:item.volume_24h="{ item }">
        <span
          >$
          {{
            parseFloat(item.prices.volume_24h.toFixed(2)).toLocaleString()
          }}</span
        >
      </template>
      <template v-slot:item.circ_supply="{ item }">
        <span
          >$ {{ parseFloat(item.circ_supply.toFixed(2)).toLocaleString() }}
          {{ item.symbol }}</span
        >
      </template> -->
    </v-data-table>
    <v-btn href="coin/1">Ola</v-btn>
  </div>
</template>


<script>
import { mapGetters } from "vuex";
export default {
  name: "Coin",
  data: () => {
    return {
        item: {},
        tags: [],
        explorers: [],
        prices: {},
        tradingPairs: [],
        page: 1,
        totalItems: 0,
        numberOfPages: 0,
        loading: true,
        options: {

        },
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
        }
        // },
        // {
        //   text: "Buy",
        //   value: "buycoin",
        //   align: "start",
        // },
        // {
        //   text: "Sell",
        //   value: "sellcoin",
        //   align: "end",
        // },
        // {
        //   text: "",
        //   value: "prices24",
        //   align: "end",
        // },
        // {
        //   text: "7d%",
        //   value: "prices7",
        //   align: "end",
        // },
        // {
        //   text: "Market Cap",
        //   value: "marketCap",
        //   align: "end",
        // },
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
      slug: ""
    }
  },

//   watch: {
//     options: {
//       handler() {
//         this.readData();
//       },
//     },
//     deep: true,
//   },

  created() {
      this.buscarCoin();
      //this.readData();
  },

  mounted(){
      this.readData();
  },
    

  methods: {
      buscarCoin(){
        let url = window.location.href
        let coin_id = url.split("/").slice(-1).pop()
        this.$request("get", `coins/${coin_id}`)
        .then((data) => {
            console.log('data', data)
            console.log(data.data[0])
            this.item = data.data[0]
            this.tags = data.data[0].nomecat.split(';')
            this.slug = data.data[0].slug
        
        })
        .catch((e) => console.log(e));
        },

    readData() {
      console.log('options', this.options)
      let myurl = window.location.href
      let coin_slug = myurl.split("/").slice(-1).pop()
      this.loading = true;
      const { page, itemsPerPage } = this.options;
      let pageNumber = page - 1;
      pageNumber = pageNumber === -1 ? 0 : pageNumber;
      console.log('pag number', pageNumber)
      console.log('slug')
      let url = 'tradingPairs/'+ coin_slug +'/type/SpotPair?size=' + itemsPerPage + '&page=' + pageNumber
      console.log('url', url)
      this.$request("get", url)
        .then((data) => {
          console.log('data -> ', data)
          //this.items1 = data.data.dados;
          this.totalItems = data.data.totalItems;
          this.numberOfPages = data.data.numberOfPages;
          console.log('total items', data.data.totalItems, 'number of pages', data.data.numberOfPages)
          
          let ids = data.data.dados.map((e) => e.marketid).toString();
          console.log('ids', ids);
          this.getPrices(ids, data.data.dados, coin_slug);
        })
        .catch((e) => console.log(e));

    },

        getPrices(ids, dados, slug) {
            this.$request("getp", `marketPairPrice?slug=${slug}&category=spot&market=${ids}`)
            .then((data) => {
                //console.log(data.data);
                let prices = Object.values(data.data).map((item) => {
                return item;
                });
                this.items1 = dados;
                prices.map((e, index) => {
                this.items1[index]["prices"] = e;
                //this.items1[index]["circ_supply"] = Object.values(data.data)[index]["circulating_supply"];
                })
                this.loading = false;
                console.log('items1',this.items1)
            })
            .catch((e) => console.log(e));
    },
    },


  computed: {
    ...mapGetters(["carts"]),
  },
};
</script>
