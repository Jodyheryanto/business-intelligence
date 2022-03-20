<template>
  <div style="margin-top: 20px;">
    <div class="row">
      <div class="col-1 col-md-1 col-lg-1">
      </div>
      <!--Start Header-->
      <!-- <app-header></app-header>
      <app-sidebar></app-sidebar> -->
      <div class="col-10 col-md-10 col-lg-10">
        <app-content></app-content>
        <div class="main-footer" style="margin-left: 0px; width: 100%;">
            <div class="footer-left">
                Copyright &copy; 2020 <div class="bullet"></div> Design By <a href="">Jody</a>
            </div>
            <div class="footer-right">
                in Development
            </div>
        </div>
      </div>
      <div class="col-1 col-md-1 col-lg-1">
      </div>
    </div>
  </div>
</template>

<script>
// import Header from "@/components/Header.vue"
// import Sidebar from "@/components/Sidebar.vue"
import Content from "@/components/ContentReport.vue"
// import store from '@/store'
export default {
  components: {
    // 'app-header': Header,
    // 'app-sidebar': Sidebar,
    'app-content': Content
  },
  mounted() {
    // if(eval(this.$cookie.get('user_success')) !== true && parseInt(this.$cookie.get('user_role')) !== 0){
    //   this.$router.replace({
    //       name: '404'
    //   })
    // }
    if(eval(this.$cookie.get('user_success')) !== true){
      this.$router.replace({
          name: 'Auth'
      })
    }
  },
}
</script>

<style scoped>
</style>