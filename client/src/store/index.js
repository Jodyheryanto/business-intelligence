import Vue from 'vue'
import Vuex from 'vuex'
import auth from './auth'
import post from './posts'
import api from './apiconfig'
import notification from './notification'
import help from './help'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
      ChartData: [],
      Data: [],
      paramWord: null,
      nama_aplikasi: null
    },
  actions: {
    async loadDataChart(context) {
      var result = await axios.get("http://127.0.0.1:5000/wordcloud?user_id=" + this.state.post.param.user_id, {
        headers: {
          Authorization: 'Bearer ' + this.state.post.param.access_token //the token is a variable which holds the token
        }
      });
      context.commit("SET_CHART", result.data.values);
    },
    async loadChartDetail(context) {
      var result = await axios.get("http://127.0.0.1:5000/getpost/" + this.state.paramWord, {
        headers: {
          Authorization: 'Bearer ' + this.state.post.param.access_token //the token is a variable which holds the token
        }
      });
      context.commit("SET_DATA", result.data.values);
    },
      // async loadLines({ commit }) {
      //   axios
      //     .get('https://api.worldbank.org/v2/countries/NOR/indicators/NY.GDP.MKTP.KD.ZG?per_page=12&MRV=30&format=json')
      //     .then(r => r.data)
      //     .then(lines => {
      //       commit('SET_LINE', lines)
      //     })
      // },
      // async getDetailBooks({ commit }) {
      //   axios
      //     .get('https://my-json-server.typicode.com/JodyHeryanto/demo/books/' + this.state.indexx)
      //     .then(r => r.data)
      //     .then(books => {
      //       commit('SET_BOOK', books)
      //     })
      // }
    },
    mutations: {
      SET_CHART(state, chart) {
        state.ChartData = chart
      },
      SET_DATA(state, data) {
        state.Data = data
      },
    },
    modules: {
      auth,
      post,
      api,
      notification,
      help
    }
})
