import { defineStore } from "pinia";
import { router } from "../helpers/router";
import axios from "axios";

export default defineStore({
  id: "auth",
  state: () => ({
    username: JSON.parse(localStorage.getItem("username")) || null,
    access_token: JSON.parse(localStorage.getItem("access_token")) || null,
    refresh_token: JSON.parse(localStorage.getItem("refresh_token")) || null,
    returnUrl: null,
  }),
  actions: {
    async login(username, password) {
      try {
        const axiosWithoutAuth = axios.create({
          baseURL: process.env.VUE_APP_API_BASE_URL,
          headers: {
            "Content-Type": "application/json",
          },
        });
        const { status, data } = await axiosWithoutAuth.post("/auth/login", {
          username,
          password,
        });
        if (status === 200) {
          const { username, access_token, refresh_token } = data;
          localStorage.setItem("username", JSON.stringify(username));
          localStorage.setItem("access_token", JSON.stringify(access_token));
          localStorage.setItem("refresh_token", JSON.stringify(refresh_token));
          router.push(this.returnUrl || "/");
        }
      } catch (err) {
        console.log(err);
      }
    },
    logout() {
      this.username = null;
      this.access_token = null;
      this.refresh_token = null;
      localStorage.removeItem("username");
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
    },
  },
});
