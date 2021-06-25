<template >
  
  <div>
    
    <v-data-table
      class="transparent" 
      :headers="headers"
      :items="items"      
    >
      <template v-slot:item.id="{ item }">
            <div class="p-2">
              <v-img 
                :src="'https://s2.coinmarketcap.com/static/img/coins/64x64/' + item.id + '.png'" 
                :alt="item.name" 
                height="50px"
                max-width="50px"
              >
              </v-img>
            </div>
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
      headers: [
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
      }],
      items: [],
    }
  },
  created(){
    this.getCoins();
  },
  methods: {
    getCoins(){ 
      this.$request("get","coins")
        .then(data => {console.log(data.data); this.items = data.data})
        .catch(e => console.log(e))
    }
  },
  computed: {
    ...mapGetters(["carts"])
  },
};
</script>
