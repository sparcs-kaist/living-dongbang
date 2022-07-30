import { defineStore } from "pinia";
import { router } from "../helpers/router";
import axios from "../helpers/axios";
export default defineStore({
  id: "auth",
  state: () => ({
    username: JSON.parse(localStorage.getItem("user")) || null,
    returnUrl: null,
  }),
  actions: {
    async login(username, password) {
      try {
        const { status, data } = await axios.post("/auth/login", {
          username,
          password,
        });
        if (status === 200) {
          this.username = data.username;
          localStorage.setItem("user", JSON.stringify(data));
          router.push(this.returnUrl || "/");
        }
      } catch (err) {
        console.log(err);
      }
    },
    logout() {
      this.username = null;
      localStorage.removeItem("user");
    },
  },
});
