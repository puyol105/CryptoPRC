<template>
  <v-app
    clipped-left
    :style="{ background: $vuetify.theme.themes[theme].background }"
  >
    <!-- <v-container/>
    <v-container/>
    <v-container/>
    <v-container/>
    <v-container/> -->

    <v-app-bar
      app
      color="#fcb69f"
      dark
      clipped-left
      src="https://c1.wallpaperflare.com/preview/297/171/764/chart-trading-courses-analysis.jpg"
    >
      <template v-slot:img="{ props }">
        <v-img
          v-bind="props"
          gradient="to top right, rgba(19,84,122,.5), rgba(128,208,199,.8)"
        ></v-img>
      </template>

      <v-app-bar-nav-icon @click="drawerState = !drawerState"></v-app-bar-nav-icon>

      <v-toolbar-title>CryptoManiac</v-toolbar-title>

      <v-spacer></v-spacer>

      <template v-slot:extension>
        <v-tabs align-center fixed-tabs dark>
          <v-tab href="/">Cryptocurrencies</v-tab>
            <v-menu offset-y>
              <template v-slot:activator="{ on, attrs }">
                <v-tab
                  v-bind="attrs"
                  v-on="on"
                >
                  Exchanges
                </v-tab>
              </template>
              <v-list>
                <v-list-item

                  v-for="(item, index) in items"
                  :key="index"
                  :href= item.href
                >
                  <v-list-item-title class="d-flex justify-center">{{ item.name }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
          <v-tab href="/outros">Outros</v-tab>
        </v-tabs>
      </template>
      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn> </v-app-bar
    ><v-navigation-drawer
      v-model="drawerState"
      app
      clipped
      color="#2A3F54"
    >
      <v-list
        nav
        dense
        dark
      >
        <v-list-item-group
          v-model="group"
          class="white--text"
        >
          <v-list-item link to="/">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>

          <v-list-item link to="/login">
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Login</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer><v-main> <router-view /> </v-main>

    

    <v-footer fixed padless dark color="#2A3F54">
      <v-row justify="center" no-gutters>
        <v-btn color="white" text rounded icon>
          <v-icon size="24px"> mdi-github </v-icon>
        </v-btn>
        <v-col class="text-center" cols="12">
          <strong>©PRC2021</strong>
        </v-col>
      </v-row>
    </v-footer>
  </v-app>
</template>

<script>
//https://picsum.photos/1920/1080?random
export default {
  name: "App",

  data: () => {
    return {
      drawer: false,
      group: null,
      items : 
      [
        {
          name : 'Spot',
          href : '/exchanges?type=spot'
        },
        
        {
          name : 'Derivatives',
          href : '/exchanges?type=derivatives'
        },

        {
          name : 'Dex',
          href : '/exchanges?type=dex'
        },

        {
          name : 'Lending',
          href : '/exchanges?type=lending'
        },

      ]

    }
    //
  },
  computed: {
    theme() {
      return this.$vuetify.theme.dark ? "dark" : "light";
    },
    drawerState: {
      get () { return this.$store.getters.drawerState },
      set (v) { return this.$store.commit('toggleDrawerState', v) }
    }
  },
};
</script>
<style>
#app {
  background-color: var(--v-background-base);
}
</style>
