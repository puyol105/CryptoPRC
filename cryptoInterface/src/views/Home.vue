<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="items"
    >

    </v-data-table>
  </div>
</template>

<script>

export default {
  name: "Home",
  data: () => {
    return {
      headers: [{
        text: "Nome",
        value: "name"
      },
      {
        text: "Symbol",
        value: "symbol"
      },
      {
        text: "Slug",
        value: "slug"
      }],
      items: []
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
  }
};
</script>
