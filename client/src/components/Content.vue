<template>
    <div class="main-content">
        <section class="section" v-if="success === true">
            <app-chart-line></app-chart-line>

            <div class="row">
                <app-chart-bar></app-chart-bar>
                <app-word-cloud></app-word-cloud>
            </div>

            <filter-data/>
            <versus-date/>
            <!-- <app-table-insight></app-table-insight> -->

            <app-table-comment></app-table-comment>

            <app-table-post></app-table-post>

            <app-result></app-result>

        </section>
        <section class="section" style="text-align: center; margin-top: 100px" v-else>
            <img src="@/assets/img/loading.gif" alt="loading">
        </section>
    </div>
</template>
<script>
import ChartLine from './ChartLine.vue'
import ChartBar from './ChartBar.vue'
//import TableInsight from './TableInsight.vue'
import TableComment from './TableComment.vue'
import Result from './Result.vue'
import TablePost from './TablePost.vue'
import WordCloud from './WordCloud.vue'
import DemoDraggableModal  from './detailWordCloud.vue'
import FilterDate from './FilterDate.vue'
import VersusDate from './VersusDate.vue'
import store from '@/store'
import moment from 'moment'
export default {
    components: {
        'app-chart-line': ChartLine,
        'app-chart-bar': ChartBar,
        //'app-table-insight': TableInsight,
        'app-table-comment': TableComment,
        'app-result': Result,
        'app-table-post': TablePost,
        'app-word-cloud': WordCloud,
        'filter-data': FilterDate,
        'versus-date': VersusDate,
        DemoDraggableModal
    },
    data(){
        return{
            success: false,
            DataPostFilter: [],
            sentiment: [],
            source: [],
            aplikasi: ''
        }
    },
    async mounted() {
        this.isBusy = true;
        // store.state.post.param.googleplay = this.$cookie.get('user_googleplay')
        // store.state.post.param.appstore = this.$cookie.get('user_appstore')
        // store.state.post.param.instagram = this.$cookie.get('user_instagram')
        // store.state.post.param.twitter = this.$cookie.get('user_twitter')
        // store.state.post.param.nama_aplikasi = this.$cookie.get('user_nama_aplikasi')
        // store.state.post.param.access_token = this.$cookie.get('user_token')
        store.state.post.param.user_id = this.$cookie.get('user_id')
        store.state.post.param.access_token = this.$cookie.get('user_token')
        var sen_length = null
        var sou_length = null
        if(eval(this.$cookie.get('filterClick')) === true){
            store.state.post.param.startDate = this.$cookie.get('startDate');
            store.state.post.param.endDate = this.$cookie.get('endDate');
            sen_length = this.$cookie.get('sentiment_length')
            sou_length = this.$cookie.get('source_length')
            for(var i=0; i<sen_length; i++){
                this.sentiment.push(this.$cookie.get('sentiment'+i))
            }
            store.state.post.param.sentiments = this.sentiment
            for(i=0; i<sou_length; i++){
                this.source.push(this.$cookie.get('source'+i))
            }
        }else{
            store.state.post.param.sentiments = [1,0]
            // this.source = ['Google Play', 'App Store', 'Instagram']
            this.source = ['Google Play', 'App Store', 'Instagram', 'Twitter']
            for(i=0; i<this.source.length; i++){
                this.$cookie.set('source'+i, this.source[i])
            }
            for(i=0; i<store.state.post.param.sentiments.length; i++){
                this.$cookie.set('sentiment'+i, this.sentiment[i])
            }
            this.$cookie.set('sentiment_length', 2);
            this.$cookie.set('source_length', 4);
            store.state.post.param.startDate = moment(this.addDays(new Date(), -30)).format('YYYY-MM-DD')
            store.state.post.param.endDate = moment(new Date()).format('YYYY-MM-DD')
        }
        try {
            await this.$store.dispatch('post/loadDataPost')
            this.fillData()
        } catch (ex) {
            this.error = "Failed to load data";
        } finally {
            this.isBusy = false;
        }
    },
    methods: {
        fillData(){
            // let data = store.state.post.DataPost.data
            let data = store.state.post.DataPost
            for(var i = 0; i < data.length; i++){
                // if(this.$cookie.get('user_role') === "0"){
                for(var k=0; k<this.source.length;k++){
                    if(data[i].sumber === this.source[k]){
                        this.DataPostFilter.push({id: data[i].id, username: data[i].user_name, user_avatar: data[i].user_avatar, post: data[i].post, tanggal_post: data[i].tanggal_post, sumber: data[i].sumber, link_review: data[i].link_review, rating: data[i].rating, sentiment: data[i].sentiment})
                    }
                }
                // }else{
                //                     for(k=0; k<this.source.length;k++){
                //                         if(data[i].sumber === this.source[k]){
                //                             this.DataPostFilter.push({id: data[i].id, username: data[i].user_name, user_avatar: data[i].user_avatar, post: data[i].post, tanggal_post: data[i].tanggal_post, sumber: data[i].sumber, link_review: data[i].link_review, rating: data[i].rating, sentiment: data[i].sentiment})
                //                         }
                //                     }
                //                 }
                //             }
                // }
            }
            store.state.post.DataPostFilter = this.DataPostFilter
            this.success = true
        },
        addDays(theDate, days) {
            return new Date(theDate.getTime() + days*24*60*60*1000);
        },
    },
}
</script>
<style>
.main-content{
    min-height: 700px;
}
</style>