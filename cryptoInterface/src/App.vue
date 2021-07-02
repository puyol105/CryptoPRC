<template>
  <v-app
    clipped-left
    :style="{ background: $vuetify.theme.themes[theme].background }"
  >
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

      <v-app-bar-nav-icon
        @click="drawerState = !drawerState"
      ></v-app-bar-nav-icon>

      <v-toolbar-title>CryptoManiac</v-toolbar-title>

      <v-spacer></v-spacer>

      <template v-slot:extension>
        <v-tabs align-center fixed-tabs dark>
          <v-tab href="/">Cryptocurrencies</v-tab>
          <v-menu offset-y>
            <template v-slot:activator="{ on, attrs }">
              <v-tab v-bind="attrs" v-on="on"> Exchanges </v-tab>
            </template>
            <v-list>
              <v-list-item
                v-for="(item, index) in items"
                :key="index"
                :href="item.href"
              >
                <v-list-item-title class="d-flex justify-center">{{
                  item.name
                }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
          <v-tab href="/tags">Tags</v-tab>
        </v-tabs>
      </template> </v-app-bar
    ><v-navigation-drawer v-model="drawerState" app clipped color="#2A3F54">
      <v-list nav dense dark>
        <!-- <v-list-item-group v-for="option in drawerOptions" :key="option.text" v-model="group" class="white--text">
          <v-list-item  v-if="option.authenticated?(!isLoged()===option.authenticated):true"  link :to="option.link?option.link:void(0)">
            <v-list-item-icon>
              <v-icon>{{option.icon}}</v-icon>
            </v-list-item-icon>
            <v-list-item-title>{{option.text}}</v-list-item-title>
          </v-list-item>
        </v-list-item-group> -->
        <v-list-item-group class="white--text">
          <v-list-item   link to="/">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
        <v-list-item-group class="white--text">
          <v-list-item  v-if="isLoged()"  link to="/Login">
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Login</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
        <v-list-item-group class="white--text">
          <v-list-item  v-if="!isLoged()"  link to="/favs">
            <v-list-item-icon>
              <v-icon>mdi-heart</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Favorites</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
        <v-list-item-group class="white--text">
          <v-list-item  v-if="!isLoged()"  @click="logout()">
            <v-list-item-icon>
              <v-icon>mdi-exit-run</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list> </v-navigation-drawer
    ><v-main> <router-view /> </v-main>

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
      drawerOptions: [
        {
          text: "Home",
          link: "/",
          icon: "mdi-home",
          // authenticated: false
        },
        {
          text: "Login",
          link: "/login",
          icon: "mdi-account",
          authenticated: false
        },
        {
          text: "Favorites",
          link: "/favs",
          icon: "mdi-heart",
          authenticated: true
        },
        {
          text: "Logout",
          link: "/",
          icon: "mdi-exit-run",
          authenticated: true
        },
      ],
      group: null,
      items: [
        {
          name: "Spot",
          href: "/exchanges/spot",
        },

        {
          name: "Derivatives",
          href: "/exchanges/derivatives",
        },

        {
          name: "Dex",
          href: "/exchanges/dex",
        },

        {
          name: "Lending",
          href: "/exchanges/lending",
        },
      ],
    };
    //
  },
  computed: {
    theme() {
      return this.$vuetify.theme.dark ? "dark" : "light";
    },
    drawerState: {
      get() {
        return this.$store.getters.drawerState;
      },
      set(v) {
        return this.$store.commit("toggleDrawerState", v);
      },
    },
  },
  methods: {
    isLoged() {
      if (this.$store.state.user)
        return Object.keys(this.$store.state.user).length === 0;
    },
    logout(){
      this.$request('post','/logout',this.$store.state.user)
        .then(() => {
          this.$router.push('/')
        })
        .catch(e => console.log(e))
      this.$store.commit("guardaNomeUtilizador",{})
    }
  },
};
</script>
<style>
#app {
  background-color: var(--v-background-base);
}
</style>
