<template>
  <v-app id="app" :style="{background: $vuetify.theme.themes[theme].background}">
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://i.pinimg.com/originals/dd/fd/f5/ddfdf5880a7acc0e4ab6e1e549e05a24.png"
          width="60"
        />
      </div>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
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