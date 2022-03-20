<template>
	<div class="col-12 col-md-12 col-lg-12">
    <div class="card">
        <div class="card-header">
            <div>
              <h4>Result</h4>
              <ul class="nav card-header-tabs pull-right"  id="myTab" role="tablist">
                  <li class="nav-item" v-for="(source, index) in sources" v-bind:key="index">
                      <a class="nav-link" @click="changeData(source)" data-toggle="tab" href="#" role="tab" aria-controls="home" aria-selected="true"><strong>{{ source }}</strong></a>
                  </li>
              </ul>
          </div>
        </div>
        <div class="card-body" width="100%" height="100%">
          <div v-if="words[0][2] != '#47C363'">
            <h4>From the data we analysis so far :</h4><br>
            <h4 style="text-align: center">
            <span style="color: red; text-align: center">We need to fix the "<strong>{{ words[0][0] }}</strong>"</span><br><br>
            </h4>
            <h5 style="text-align: justify">
            Here is the sample review from our customer "{{ sample['post'] }}" by {{ sample['user_name'] }}
            </h5>
          </div>
          <div v-else>
            <h4>From the data we analysis so far :</h4><br>
            <h4 style="text-align: center">
            <span style="color: green; text-align: center">We need to improve the "<strong>{{ words[0][0] }}</strong>"</span><br><br>
            </h4>
            <h5 style="text-align: justify">
            Here is the sample review from our customer "{{ sample['post'] }}" by {{ sample['user_name'] }}
            </h5>
          </div>
        </div>
    </div>
	</div>
</template>

<script>
import store from '@/store'
export default {
	data() {
		return {
      data: [],
      words: [],
      test: [],
      color: '',
      source: '',
      sources: [],
      sample: [],
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
    async fillData(){
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
        store.state.paramWord = this.words[0][4]
        this.isBusy = false;
        try {
            await this.$store.dispatch('loadChartDetail')
            this.sample = store.state.Data
        } catch (ex) {
            this.error = "Failed to load data";
        } finally {
            this.isBusy = false;
        }
        this.isBusy = false;
        this.success = true
    }
  }
}
</script>