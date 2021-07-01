import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Exchanges from "../views/Exchanges.vue";
import Coin from "../views/Coin.vue";
import Tags from "../views/Tags.vue";


Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/exchanges",
    name: "Exchanges",
    component: Exchanges,
  },
  {
    path: "/coin/:id",
    name: "Coin",
    component: Coin,
  },
  {
    path: "/tags/:tag/:id",
    name: "Category",
    component: Tags,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
