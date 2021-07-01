import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    drawerState: false
  },
  mutations: {
    toggleDrawerState (state, data) {
      state.drawerState = data
    }
  },
  actions: {},
  modules: {},
  getters: {
    drawerState: (state) => state.drawerState
  },
});