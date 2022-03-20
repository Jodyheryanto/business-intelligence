<template>
  <div>
    <app-login></app-login>
    <demo-adaptive-modal/>
  </div>
</template>
<script>
import login from '../components/Login.vue'
import DemoAdaptiveModal from '../components/Register.vue'
export default {
  components: {
    'app-login': login,
    DemoAdaptiveModal
  },
  mounted() {
    if(eval(this.$cookie.get('user_success')) === true){
      this.$router.replace({
          name: 'Home'
      })
    }
  },
}
</script>