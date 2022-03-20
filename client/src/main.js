import Vue from 'vue'
import App from './App.vue'
import VueJsModal from 'vue-js-modal'
import { EventBus } from './utils/eventbus'
import router from './router'
import echarts from 'echarts'
import { BootstrapVue } from 'bootstrap-vue'
import VCalendar from 'v-calendar';
import VueWordCloud from 'vuewordcloud';
import store from './store'
import VueIziToast from 'vue-izitoast';
//import axios from 'axios'
import "izitoast/dist/css/iziToast.css";
import Chart from 'vue2-frappe'
import VueMq from 'vue-mq'
import CKEditor from "@ckeditor/ckeditor5-vue2";

Vue.use(CKEditor);

var VueCookie = require('vue-cookie');
Vue.use(VueCookie);

Vue.use(VueMq, {
  breakpoints: {
    mobile: 450,
    tablet: 900,
    laptop: 1250,
    desktop: Infinity,
  }
})

Vue.use(Chart)

Vue.use(VueIziToast);

//axios.defaults.baseURL = 'https://dev.lenna.ai/auth/public/'

Vue.component(VueWordCloud.name, VueWordCloud);

// Use v-calendar & v-date-picker components
Vue.use(VCalendar, {
  componentPrefix: 'vc'
});

// Install BootstrapVue
Vue.use(BootstrapVue)

Vue.prototype.$echarts = echarts

require('echarts-wordcloud')


Vue.use(VueJsModal, {
  dialog: true,
  dynamic: true,
  dynamicDefaults: {
    foo: 'foo'
  }
})

Vue.config.productionTip = false;
Vue.prototype.$eventBus = EventBus;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')