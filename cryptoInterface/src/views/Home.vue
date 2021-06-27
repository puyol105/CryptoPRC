<template >
  
  <div>
    
    <v-data-table
      class="transparent" 
      :headers="headers1"
      :items="items1"      
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
      <template v-slot:item.pricesP="{ item }">
           <span>$ {{parseFloat(item.prices.price.toFixed(2)).toLocaleString()}}</span>
      </template>
      <template v-slot:item.prices24="{ item }">
           <span>{{parseFloat(item.prices.percent_change_24h.toFixed(2)).toLocaleString()}} %</span>
      </template>
      <template v-slot:item.prices7="{ item }">
           <span>{{parseFloat(item.prices.percent_change_7d.toFixed(2)).toLocaleString()}} %</span>
      </template>
      <template v-slot:item.marketCap="{ item }">
           <span>{{parseFloat(item.prices.market_cap.toFixed(2)).toLocaleString()}}</span>
      </template>
      <template v-slot:item.volume="{ item }">
           <span>$ {{parseFloat(item.prices.volume_24h.toFixed(2)).toLocaleString()}}</span>
      </template>

    </v-data-table>

  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "Home",
  data: () => {
    return {
      headers1: [
      {
        text: "Logo",
        value: "id",
        align: 'start',
        sortable: false
      },
      {
        text: "Nome",
        value: "name",
        align: 'start'
      },
      {
        text: "Symbol",
        value: "symbol",
        align: 'center',
        sortable: false
      },
      {
        text: "Slug",
        value: "slug",
        align: 'end',
        sortable: false
      },
      {
        text: "Price",
        value: "pricesP",
        align: 'end',
        sortable: false
      },
      {
        text: "24h%",
        value: "prices24",
        align: 'end',
        sortable: false
      },
      {
        text: "7d%",
        value: "prices7",
        align: 'end',
        sortable: false
      },
      {
        text: "Market Cap",
        value: "marketCap",
        align: 'end',
        sortable: false
      },
      {
        text: "Volume (24h)",
        value: "volume",
        align: 'end',
        sortable: false
      }],
      items1: [],

    }



  },
  created(){
    this.getCoins();
    console.log('final', this.items1)
  },
  methods: {
    getCoins(){ 
      this.$request("get","coins")
        .then(data => { 
          //console.log(data.data); 
          //this.items1 = data.data;
          let ids = data.data.map(e => e.id ).toString()
          //console.log('ids', ids)
          this.getPrices(ids, data.data)
        })
        .catch(e => console.log(e))
    },
    getPrices(ids, dados){
      this.$request("getp",`coinPrice?id=${ids}`)
        .then(data => {
                        //console.log(data.data); 
                        let prices = Object.values(data.data).map( item => {
                          return(item.quote.USD)
                        })
                        this.items1 = dados
                        prices.map( (e,index) => {
                          this.items1[index]["prices"] = e
                        })
                  
        })
        .catch(e => console.log(e))
    }

  },
  computed: {
    ...mapGetters(["carts"])
  },
};
</script>
