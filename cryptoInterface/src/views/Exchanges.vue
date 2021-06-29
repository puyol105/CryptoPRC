<template>
  <div>
    <v-data-table class="transparent" :headers="headers1" :items="items1">
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
        <span> {{ item.name }} ( {{ item.symbol }} )</span>
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
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "Exchanges",
  data: () => {
    return {}
  },
  created() {
    console.log('entrei-------------------------------')
  },

  methods: {

  },

  computed: {
    ...mapGetters(["carts"]),
  },
};
</script>
