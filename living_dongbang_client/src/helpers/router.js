import { createRouter, createWebHistory } from "vue-router";
import useAuthStore from "../stores/auth.store";
export const router = createRouter({
  history: createWebHistory(),
  linkActiveClass: "active",
  routes: [
    { path: "/login", component: () => import("../views/LoginPage.vue") },
    { path: "/logout", component: () => import("../views/LogoutPage.vue") },
    { path: "/", component: () => import("../views/FrontPage.vue") },
  ],
});

router.beforeEach(async (to) => {
  const publicPages = ["/login"];
  const authRequired = !publicPages.includes(to.path);
  const auth = useAuthStore();
  if (authRequired && !auth.username) {
    auth.returnUrl = to.fullPath;
    router.push("/login");
  }
});
