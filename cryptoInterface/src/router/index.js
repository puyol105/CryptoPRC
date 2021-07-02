import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Exchanges from "../views/Exchanges.vue";
import Coin from "../views/Coin.vue";
import Tag from "../views/Tag.vue";
import Exchange from "../views/Exchange.vue";
import Tags from "../views/Tags.vue";
import store from "../store";


Vue.use(VueRouter);

const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch((err) => err);
};

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/exchanges/:type",
    name: "Exchanges",
    component: Exchanges,
  },
  {
    path: "/exchange/:id",
    name: "Exchange",
    component: Exchange,
  },
  {
    path: "/coin/:id",
    name: "Coin",
    component: Coin,
  },
  {
    path: "/tag/:tag/:id",
    name: "Tag",
    component: Tag,
  },
  {
    path: "/tags",
    name: "Tags",
    component: Tags,
  },
  {
    path: "/favs",
    name: "Favs",
    component: () => import("../views/Favs.vue"),
  },
  
  {
    path: "/login",
    name: "Login",
    component: () => import("../views/Login.vue"),
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

router.beforeEach((to, from, next) => {
  if (to.name === 'Login'){
    store.commit('setToken', null)
  }
  if (to.matched.some(record => record.meta.requiresAuth)){
    if (store.state.token){
      next()
    } else{
      next({
        name: 'Login'
      })
    }
  } else {
    next()
  }
})

export default router;
