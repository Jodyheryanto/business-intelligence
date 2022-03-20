<template>
  <div class="main-wrapper">
    <modal-ubah-notif/>
    <modal-ubah-help/>
    <modal-create-notif/>
    <modal-create-help/>
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
import Content from '../components/ContentSupportU.vue'
// import Footer from '../components/Footer.vue'
import ubahNotif from '../components/UbahNotif.vue'
import ubahHelp from '../components/UbahHelp.vue'
import createNotif from '../components/CreateNotif.vue'
import createHelp from '../components/CreateHelp.vue'
// import store from '@/store'
export default {
  components: {
    'app-header': Header,
    'app-content': Content,
    'modal-ubah-notif': ubahNotif,
    'modal-ubah-help': ubahHelp,
    'modal-create-notif': createNotif,
    'modal-create-help': createHelp
  },
  data () {
    return {
      
    }  
  },
  mounted() {
    if(eval(this.$cookie.get('user_success')) !== true && this.$cookie.get('user_role') !== 2){
      this.$router.replace({
          name: '404'
      })
    }
  },
}
</script>