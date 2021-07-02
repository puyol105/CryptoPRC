<template>

  <div>
      <h1>
        {{this.nametag}}
      </h1>
    
      <v-data-table 
      class="transparent" 
      :headers="headers1" 
      :items="items1"
      :page="page"
      :pageCount="numberOfPages"
      :options.sync="options"
      :server-items-length="totalItems"
      :loading="loading"
      
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
      <template v-slot:item.name="{ item }">
        <a :href="`/coin/${item.slug}`"> {{ item.name }} ( {{ item.symbol }} )
          
        </a>
      </template>
      <template v-slot:item.pricesP="{ item }">
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
      nametag: '',
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
          text: "Price",
          value: "pricesP",
          align: "end",
        },
        {
          text: "24h%",
          value: "prices24",
          align: "end",
        },
        {
          text: "7d%",
          value: "prices7",
          align: "end",
        },
        {
          text: "Market Cap",
          value: "marketCap",
          align: "end",
        },
        {
          text: "Volume (24h)",
          value: "volume_24h",
          align: "end",
        },
        {
          text: "Circulation Supply",
          value: "circ_supply",
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
    console.log("final", this.items1);
  },
  methods: {
    readData() {
      console.log('readData')
      let myurl = window.location.href
      let tag_info = myurl.split("/").reverse()
      //let tag_type = myurl.split("/").slice(-1)[-1]

      console.log('tag_id', tag_info)

      this.loading = true;
      const { page, itemsPerPage } = this.options;
      let pageNumber = page - 1;
      pageNumber = pageNumber === -1 ? 0 : pageNumber;
      
      let url = 'tags/' + tag_info[1] + '/' + tag_info[0] +'?size=' + itemsPerPage + '&page=' + pageNumber
      console.log('url', url)

      this.$request("get", url)
        .then((data) => {
          console.log('data -> ', data)
          //this.items1 = data.data.dados;
          this.totalItems = data.data.totalItems;
          this.numberOfPages = data.data.numberOfPages;
          this.nametag = data.data.dados[0]['nametag']
          console.log('nametag', this.nametag)
          console.log('total items', data.data.totalItems, 'number of pages', data.data.numberOfPages)
          
          let ids = data.data.dados.map((e) => e.id).toString();
          console.log('ids')

          this.getPrices(ids, data.data.dados);
        })
        .catch((e) => console.log(e));

    },

    getPrices(ids, dados) {
      this.$request("getp", `coinPrice?id=${ids}`)
        .then((data) => {
          //console.log(data.data);
          let prices = Object.values(data.data).map((item) => {
            return item.quote.USD;
          });
          this.items1 = dados;
          prices.map((e, index) => {
            this.items1[index]["prices"] = e;
            this.items1[index]["circ_supply"] = Object.values(data.data)[index]["circulating_supply"];
          })
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
