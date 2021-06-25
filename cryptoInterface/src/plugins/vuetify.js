import Vue from "vue";
import Vuetify from "vuetify/lib";


Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: "#603F59",
        secondary: "#b0bec5",
        accent: "#8c9eff",
        error: "#b71c1c",
        background: "#b8cfcd",
      },
      dark: {
        primary: "#603F59", 
        background: "603F59",
      },
    },
    options: {
      customProperties: true
    },
  },
});
