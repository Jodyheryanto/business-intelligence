<template>
    <div class="main-wrapper">
        <!-- penggunaan component yang telah diinisialisasi -->
        <app-header></app-header>
        <div class="main-content w-100 ">
            <h4 class="text-center mb-4">FAQ about Lenna Analytic</h4>
            <section class="section" v-if="success == true">
                <div class="accordion" role="tablist" v-for="(data, index) in items" v-bind:key="index">
                    <b-card no-body class="mb-1">
                        <b-card-header header-tag="header" class="p-1" role="tab">
                            <b-button block v-b-toggle="'accordion-' + data.id" variant="info"><h4 class="text-white">{{ data.title }}</h4></b-button>
                        </b-card-header>
                        <b-collapse :id="'accordion-' + data.id" accordion="my-accordion" role="tabpanel">
                            <b-card-body>
                            <b-card-text><h6 v-html="data.description"></h6></b-card-text>
                            </b-card-body>
                        </b-collapse>
                    </b-card>
                </div>
            </section>
        </div>
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
// import Avatar from 'vue-avatar'
import store from '@/store'
import Header from '../components/Header.vue'
export default {
  components: {
    //inisialisasi component
    'app-header': Header,
  },
  data(){
    return{
        items: [],
        success: false
    }
  },
  async mounted() {
    this.isBusy = true;
    store.state.help.param.access_token = this.$cookie.get('user_token')
    this.role = parseInt(this.$cookie.get('user_role'))
    try {
        await this.$store.dispatch('help/loadDataHelp')
        this.fillData()
    } catch (ex) {
        this.error = "Failed to load data";
    } finally {
        this.isBusy = false;
    }
    if(eval(this.$cookie.get('user_success')) !== true){
      this.$router.replace({
          name: 'Auth'
      })
    }
  },
  methods: {
    fillData(){
        let data = store.state.help.DataHelp
        for(var i = 0; i < data.length; i++){
            this.items.push({id: data[i].id, title: data[i].title, description: data[i].description})
        }
        this.success = true
    },
  },
}
</script>
