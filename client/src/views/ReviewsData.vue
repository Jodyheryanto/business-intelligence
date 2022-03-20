<template>
  <div class="main-wrapper">
    <!-- penggunaan component yang telah diinisialisasi -->
    <app-header></app-header>
    <app-sidebar></app-sidebar>
    <app-content></app-content>
    <app-footer></app-footer>
  </div>
</template>

<script>
//import per component
import Header from '../components/Header.vue'
import Sidebar from '../components/Sidebar.vue'
import Content from '../components/ContentReviews.vue'
import Footer from '../components/Footer.vue'
// import store from '@/store'
export default {
  components: {
    //inisialisasi component
    'app-header': Header,
    'app-sidebar': Sidebar,
    'app-content': Content,
    'app-footer': Footer
  },
  data () {
    return {
      
    }  
  },
  mounted() {
    // if(eval(this.$cookie.get('user_success')) !== true && parseInt(this.$cookie.get('user_role')) !== 0){
    //   this.$router.replace({
    //       name: '404'
    //   })
    // }
    if(eval(this.$cookie.get('user_success')) !== true && this.$cookie.get('user_role') !== 2){
      this.$router.replace({
          name: '404'
      })
    }
  },
}
</script>