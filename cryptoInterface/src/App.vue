<template>
  <v-app id="app" :style="{background: $vuetify.theme.themes[theme].background}">
    <v-container/>
    <v-container/>
    <v-container/>
    <v-container/>
    <v-container/>
    <v-container/>
    <v-app-bar
      absolute
      color="#fcb69f"
      dark
      shrink-on-scroll
      src="https://c1.wallpaperflare.com/preview/297/171/764/chart-trading-courses-analysis.jpg"
      scroll-target="#scrolling-techniques-2"
    >
      <template v-slot:img="{ props }">
        <v-img
          v-bind="props"
          gradient="to top right, rgba(19,84,122,.5), rgba(128,208,199,.8)"
        ></v-img>
      </template>

      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>CryptoManiac</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn >
        Exchanges
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>
    <v-sheet
      id="scrolling-techniques-2"
      class="overflow-y-auto"
      max-height="800"
      color="background"
    >
      <v-container style="height: 1000px;"><v-main>
      <router-view />
    </v-main></v-container>
    </v-sheet>

    <v-footer 
      fixed 
      padless
      dark
    >
    <v-row
      justify="center"
      no-gutters
    >
    <v-btn
        color="white"
        text
        rounded
        icon
      >
        <v-icon size="24px">
            mdi-github
          </v-icon>
      </v-btn>
    <v-col
      class="text-center"
      cols="12"
    >
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

  data: () => ({
    //
  }),
  computed:{
    theme(){
      return (this.$vuetify.theme.dark) ? 'dark' : 'light'
    }
  }
};
</script>
<style>
#app {
  background-color: var(--v-background-base);
}
</style>