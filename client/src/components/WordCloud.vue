<template>
	<div class="col-12 col-md-6 col-lg-6">
    <div class="card">
        <div class="card-header">
            <div>
              <h4>Trending Keywords</h4>
              <ul class="nav card-header-tabs pull-right"  id="myTab" role="tablist">
                  <li class="nav-item" v-for="(source, index) in sources" v-bind:key="index">
                      <a class="nav-link" @click="changeData(source)" data-toggle="tab" href="#" role="tab" aria-controls="home" aria-selected="true"><strong>{{ source }}</strong></a>
                  </li>
              </ul>
          </div>
        </div>
        <div class="card-body" width="100%" height="100%">
          <vue-word-cloud :words="words" font-family="arial" style="position: relative; min-height: 327px; width: 100%;">
            <template slot-scope="{text, weight, word}">
              <div :title="word[0] + '\n' + word[1]" :style="'cursor: pointer;' + 'color:' + word[2]" @click="onWordClick(word[3], word[4])">
                {{ text }}
              </div>
            </template>
          </vue-word-cloud>
          <p class="badge badge-success">positive</p>
          <!-- <p class="badge badge-secondary">neutral</p> -->
          <p class="badge badge-danger">negative</p>
        </div>
    </div>
	</div>
</template>

<script>
import VueWordCloud from 'vuewordcloud';
import store from '@/store'
export default {
  components: {
    'vue-word-cloud' : VueWordCloud
  },
	data() {
		return {
      data: [],
      words: [],
      test: [],
      color: '',
      source: '',
      sources: [],
		}
  },
  async mounted() {
      this.isBusy = true;
      store.state.post.param.access_token = this.$cookie.get('user_token')
      store.state.post.param.user_id = this.$cookie.get('user_id')
      this.sources = []
      this.source = this.$cookie.get('source0');
      var sou_length = this.$cookie.get('source_length')
      for(var i=0; i<sou_length; i++){
          this.sources.push(this.$cookie.get('source'+i))
      }
      try {
          await this.$store.dispatch('loadDataChart')
          this.fillData()
      } catch (ex) {
          this.error = "Failed to load data";
      } finally {
          this.isBusy = false;
      }
  },
  methods: {
    changeData(source){
        this.source = source;
        this.fillData()
    },
    async onWordClick(index, id) {
        this.$eventBus.$emit("datafromwordCloud2", this.words[index]);
        store.state.paramWord = id
        this.isBusy = false;
        try {
            await this.$store.dispatch('loadChartDetail')
            this.fillDetail()
        } catch (ex) {
            this.error = "Failed to load data";
        } finally {
            this.isBusy = false;
        }
    },
    fillDetail(){
      this.$eventBus.$emit("datafromwordCloud", store.state.Data);
      this.$modal.show("example-draggable");
    },
    fillData(){
        let data = store.state.ChartData
        var color = ''
        this.words = []
        var j = 0
        for(var i = 0; i < data.length; i++){
          if(data[i].sumber === this.source){
            if(data[i].sentiment === 1){
              color = '#47C363'
              // }else if(data[i].sentiment === 1){
              //   color = '#CDD3D8'
            }else{
              color = '#FC544B'
            }
            this.words.push([data[i].word,data[i].count, color, j, data[i].link_review])
            this.data.push(data[i])
            j++
          }
        }
        this.success = true
    }
  }
}
</script>