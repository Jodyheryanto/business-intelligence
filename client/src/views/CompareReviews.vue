<template>
  <div class="main-wrapper">
    <!-- penggunaan component yang telah diinisialisasi -->
    <app-header></app-header>
    <app-sidebar></app-sidebar>
    <!-- <app-content v-if="success == true"></app-content> -->
    <div class="main-content">
        <loading :active.sync="isLoading" 
                :is-full-page="fullPage" :opacity="0" :z-index="1"></loading>
        <section class="section" v-if="success == true">
            <compare-list></compare-list>

            <div class="row">
                <div class="col-12 col-md-12 col-lg-12">
                    <div class="card">
                        <div class="card-header d-block text-center">
                            <h4>-- Sentiment History Versus --</h4>
                        </div>
                    </div>        
                </div>
            </div>

            <div class="row">
                <div class="col-12 col-lg-6"><app-chart-line1></app-chart-line1></div>
                <div class="col-12 col-lg-6"><app-chart-line2></app-chart-line2></div>
            </div>

            <!-- <div class="row">
                <app-chart-bar></app-chart-bar>
                <app-chart-bar></app-chart-bar>
                <app-word-cloud></app-word-cloud>
            </div> -->

            <demo-draggable-modal/>
            <filter-data/>
            <versus-date/>
            <!-- <app-table-insight></app-table-insight> -->
            <div class="row">
                <div class="col-12 col-md-12 col-lg-12">
                    <div class="card">
                        <div class="card-header d-block text-center">
                            <h4>-- Post Count By User Versus --</h4>
                        </div>
                    </div>        
                </div>
            </div>
            <div class="row">
                <app-table-comment1 class="col-12 col-lg-6"></app-table-comment1>
                <app-table-comment2 class="col-12 col-lg-6"></app-table-comment2>
            </div>

            <div class="row">
                <div class="col-12 col-md-12 col-lg-12">
                    <div class="card">
                        <div class="card-header d-block text-center">
                            <h4>-- Post Data Versus --</h4>
                        </div>
                    </div>        
                </div>
            </div>

            <div class="row">
                <app-table-post1 class="col-12 col-lg-6"></app-table-post1>
                <app-table-post2 class="col-12 col-lg-6"></app-table-post2>
            </div>
            

        </section>
    </div>
    <app-footer></app-footer>
  </div>
  <!-- <div class="d-flex justify-content-center align-items-center" style="transform: translateY(80%);" v-else>
      <img src="@/assets/img/loading.gif" alt="loading">
  </div> -->
</template>

<script>
//import per component
import Header from '../components/Header.vue'
import Sidebar from '../components/SidebarCompare.vue'
// import Content from '../components/ContentCompare.vue'
import ChartLine1 from '../components/CompareChartLine1.vue'
import ChartLine2 from '../components/CompareChartLine2.vue'
// import ChartBar from './ChartBar.vue'
//import TableInsight from './TableInsight.vue'
import TableComment1 from '../components/CompareTableComment1.vue'
import TableComment2 from '../components/CompareTableComment2.vue'
import TablePost1 from '../components/CompareTablePost1.vue'
import TablePost2 from '../components/CompareTablePost2.vue'
// import WordCloud from './WordCloud.vue'
import CompareList from '../components/CompareList.vue'
// import DemoDraggableModal  from '../components/detailWordCloud.vue'
import FilterDate from '../components/FilterDate.vue'
import VersusDate from '../components/VersusDate.vue'
import Footer from '../components/Footer.vue'
import store from '@/store'
// Import component
import Loading from 'vue-loading-overlay';
// Import stylesheet
import 'vue-loading-overlay/dist/vue-loading.css';
// import store from '@/store'
export default {
  components: {
    //inisialisasi component
    'app-header': Header,
    'app-sidebar': Sidebar,
    // 'app-content': Content,
    'app-chart-line1': ChartLine1,
    'app-chart-line2': ChartLine2,
    // 'app-chart-bar': ChartBar,
    //'app-table-insight': TableInsight,
    'app-table-comment1': TableComment1,
    'app-table-comment2': TableComment2,
    'app-table-post1': TablePost1,
    'app-table-post2': TablePost2,
    // 'app-word-cloud': WordCloud,
    'filter-data': FilterDate,
    'versus-date': VersusDate,
    'compare-list': CompareList,
    'app-footer': Footer,
    Loading
  },
  data () {
    return {
      success: false,
      isLoading: true,
      fullPage: false
    }  
  },
  async mounted() {
    // if(eval(this.$cookie.get('user_success')) !== true && parseInt(this.$cookie.get('user_role')) !== 0){
    //   this.$router.replace({
    //       name: '404'
    //   })
    // }
    if(eval(this.$cookie.get('user_success')) !== true || this.$cookie.get('user_role') != 1){
      this.$router.replace({
          name: 'Auth'
      })
    }else{
      this.isBusy = true;
      store.state.post.param.access_token = this.$cookie.get('user_token')
      store.state.post.param.user_id = this.$cookie.get('user_id')
      // store.state.post.param.startDate = this.$cookie.get('compare_start1')
      // store.state.post.param.endDate = this.$cookie.get('compare_end1')
      // store.state.post.param.startDate = this.$cookie.get('compare_start2')
      // store.state.post.param.endDate = this.$cookie.get('compare_end2')
      store.state.post.param.sentiments = [1,0]
      let param_aplikasi = [
      {
          startDate: this.$cookie.get('compare_start1'),
          endDate: this.$cookie.get('compare_end1')
      },
      {
          startDate: this.$cookie.get('compare_start2'),
          endDate: this.$cookie.get('compare_end2')
      }]
      for(var i=0; i<2; i++){
        store.state.post.param.startDate = param_aplikasi[i].startDate
        store.state.post.param.endDate = param_aplikasi[i].endDate
        try {
            // if(store.state.indexx === null){
                await this.$store.dispatch('post/loadDataPost')
                this.fillData(i)
            // }else{
                // await this.$store.dispatch('loadReview')
                // this.fillData()
            // }
        } catch (ex) {
            this.error = "Failed to load data";
        } finally {
            this.isBusy = false;
        }
      }
      this.success = true
      this.isLoading = false
    }
  },
  methods: {
    async fillData(param) {
        if(param == 0){
          store.state.post.DataCompare1 = store.state.post.DataPost
        }else{
          store.state.post.DataCompare2 = store.state.post.DataPost
        }
    }
  },
}
</script>