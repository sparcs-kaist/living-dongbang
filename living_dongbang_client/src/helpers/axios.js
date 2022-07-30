import axios from "axios";
import useAuthStore from "../stores/auth.store";

export default axios.create({
  baseURL: process.env.VUE_APP_API_BASE_URL,
  headers: {
    Authorization: `Bearer ${useAuthStore().access_token}`,
    "Content-Type": "application/json",
  },
});
