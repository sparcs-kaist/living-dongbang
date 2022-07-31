import { defineStore } from "pinia";
import { router } from "../helpers/router";
import axios from "axios";

export default defineStore({
  id: "auth",
  state: () => ({
    username: null,
    access_token: null,
    refresh_token: null,
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
          this.username = username;
          this.access_token = access_token;
          this.refresh_token = refresh_token;
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
    },
  },
});
