<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://i.pinimg.com/originals/dd/fd/f5/ddfdf5880a7acc0e4ab6e1e549e05a24.png"
          To enable classic snap support, enter the following to create a symbolic link between /var/lib/snapd/snap and /snaptransition="scale-transition"
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
};
</script>
