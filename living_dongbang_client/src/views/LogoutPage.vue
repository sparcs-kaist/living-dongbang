<script>
import useAuthStore from "../stores/auth.store";
import { router } from "../helpers/router";
const authStore = useAuthStore();
authStore.logout();
router.push("/");

export default {
  name: "LogoutPage",
};
</script>
