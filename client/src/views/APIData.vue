<template>
  <div class="main-wrapper">
    <modal-ubah-api/>
    <!-- penggunaan component yang telah diinisialisasi -->
    <app-header></app-header>
    <!-- <app-sidebar></app-sidebar> -->
    <app-content style="width: 100%"></app-content>
    <div class="main-footer" style="margin-left: 0px; width: 100%;">
        <div class="footer-left">
            Copyright &copy; 2020 <div class="bullet"></div> Design By <a href="">Jody</a>
        </div>
        <div class="footer-right">
            in Development
        </div>
    </div>
  </div>
</template>

<script>
//import per component
import Header from '../components/Header.vue'
// import Sidebar from '../components/Sidebar.vue'
import Content from '../components/ContentAPI.vue'
// import Footer from '../components/Footer.vue'
// import store from '@/store'
import ubahAPI from '../components/UbahAPIConfig.vue'
export default {
  components: {
    //inisialisasi component
    'app-header': Header,
    // 'app-sidebar': Sidebar,
    'app-content': Content,
    'modal-ubah-api': ubahAPI
    // 'app-footer': Footer
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