<template>
    <div style="min-height: 500px;">
        <loading :active.sync="isLoading" 
                :is-full-page="fullPage" :opacity="0" :z-index="1"></loading>
        <section class="section" v-if="success == true">
            <div class="section-header">
            <h1>Report Reviews</h1>
            </div>
            <filter-data/>
            <div class="section-body">
                <div class="row">
                    <div class="col-12 col-md-4 col-lg-4">
                        <div class="card">
                            <div class="card-header">
                                <h4>Sentiments Total</h4>
                            </div>
                            <div class="card-body" style="height: 268px; text-align: center">
                                <apexchart type="pie" style="margin-top: 30px" height="150" :options="chartOptions" :series="series" v-if="success === true"></apexchart>
                                <h3 style="color: red; margin-top: 50px" v-else>Data review tidak ada</h3>
                            </div>
                        </div>
                    </div>
                    <div class="col-12 col-md-4 col-lg-4">
                        <div class="card">
                            <div class="card-header">
                                <h4>Post Values</h4>
                            </div>
                            <div class="card-body" style="height: 268px; text-align: center">
                                <apexchart v-if="success === true" class="chart" type="bar" height="200" style="padding: 10px;" :options="chartOptions2" :series="series2"></apexchart>
                                <h3 style="color: red; margin-top: 50px" v-else>Data review tidak ada</h3>
                            </div>
                        </div>
                    </div>
                    <div class="col-12 col-md-4 col-lg-4">
                        <div class="card">
                            <div class="card-header">
                                <h4>Total Post Come in</h4>
                            </div>
                            <div class="card-body" style="height: 268px; text-align: center">
                                <div v-if="success === true" style="margin-top: 20px"><h1>{{ total_post }}</h1><h4>Post</h4></div>
                                <div v-else style="margin-top: 20px"><h1 style="color: red">0</h1><h4>Post</h4></div>
                            </div>
                        </div>
                    </div>
                </div> 
                <div class="row">
                <div class="col-12 col-md-12 col-lg-12">
                    <div class="card">
                        <div class="card-header">
                            <h4>Post Count by User</h4>
                        </div>
                        <div class="card-body" style="text-align: center">
                            <div v-if="item_comments.length > 0" :class="styleTable()">
                                <b-table striped hover :items="item_comments" :fields="fields2">
                                    <template v-slot:cell(account)="data">
                                        <img :src="data.value.user_avatar" :alt="data.value.user_avatar" width="50" height="50" style="margin-top: 10px;">
                                        <div style="margin-top: 5px;">{{ data.value.username }}</div>
                                    </template>
                                    <template v-slot:cell(sentiment)="data">
                                        <i class="fas fa-smile" style="color: #47C363;"></i>&nbsp;{{ data.value.positive }}<br>
                                        <i class="fas fa-frown" style="color: #FC544B;"></i>&nbsp;{{ data.value.negative }}
                                    </template>
                                </b-table>
                            </div>
                            <h3 style="color: red" v-else>Data review tidak ada</h3>
                        </div>
                    </div>
                </div>
                </div>
                <div class="row">
                <div class="col-12 col-md-12 col-lg-12">
                    <div class="card">
                        <div class="card-header">
                            <h4>Post Comments</h4>
                        </div>
                        <div class="card-body" style="text-align: center">
                            <div v-if="item_posts.length > 0" :class="styleTable()">
                                <b-table striped hover :items="item_posts" :fields="fields">
                                    <template v-slot:cell(account)="data">
                                        <img :src="data.value.user_avatar" :alt="data.value.user_avatar" width="50" height="50" style="margin-top: 10px;">
                                        <div style="margin-top: 5px;">{{ data.value.username }}</div>
                                    </template>
                                    <template v-slot:cell(sumber)="data">
                                        <a :href="item_posts[data.index].link_review" target="_blank">{{ data.value }}</a>
                                    </template>
                                    <template v-slot:cell(sentiment)="data">
                                        <div v-if="data.value === 0">
                                            <p class="badge badge-danger">negative</p>
                                        </div>
                                        <div v-if="data.value === 1">
                                            <p class="badge badge-success">positive</p>
                                        </div>
                                        <!-- <div v-if="data.value === 2">
                                            <p class="badge badge-success">positive</p>
                                        </div> -->
                                    </template>
                                </b-table>
                            </div>
                            <h3 style="color: red" v-else>Data review tidak ada</h3>
                        </div>
                    </div>
                </div>
                </div>
            </div>
        </section>
    </div>
</template>
<script>
import store from '@/store'
import FilterDate from './FilterDate.vue'
import VueApexCharts from 'vue-apexcharts'
// Import component
import Loading from 'vue-loading-overlay';
// Import stylesheet
import 'vue-loading-overlay/dist/vue-loading.css';
export default {
    components: {
        'filter-data': FilterDate,
        apexchart: VueApexCharts,
        Loading
    },
    data() {
        return {
        // Note 'isActive' is left out and will not appear in the rendered table
        series2: [{
            data: []
        }],
        chartOptions2: {
            chart: {
            type: 'bar',
            height: 380
            },
            plotOptions: {
            bar: {
                horizontal: true,
            }
            },
            dataLabels: {
            enabled: false
            },
            xaxis: {
            categories: ['Positive', 'Negative'],
            }
        },
        series: [],
        chartOptions: {
            chart: {
            width: 380,
            type: 'pie',
            },
            labels: ['Positive', 'Negative'],
            responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                width: 200
                },
                legend: {
                position: 'bottom'
                }
            }
            }]
        },
        success: false,
        success2: false,
        isLoading: true,
        fullPage: false,
        count: 0,
        field_names: ['account'],
        fields: [
            {
            key: 'account',
            label: 'Account',
            sortable: true
            },
            {
            key: 'post',
            label: 'Post',
            sortable: true
            },
            {
            key: 'tanggal_post',
            label: 'Date',
            sortable: true
            },
            {
            key: 'sumber',
            label: 'Source',
            sortable: true
            },
            {
            key: 'aplikasi',
            label: 'Aplikasi'
            },
            {
            key: 'rating',
            label: 'Rating',
            sortable: true
            },
            {
            key: 'sentiment',
            label: 'Sentiment'
            }
        ],
        fields2: [
            {
            key: 'account',
            label: 'Account',
            sortable: true
            },
            {
            key: 'post',
            label: 'Post',
            sortable: true
            },
            {
            key: 'engagement',
            label: 'Engagement',
            sortable: true
            },
            {
            key: 'sentiment',
            label: 'Sentiment'
            },
            {
            key: 'sumber',
            label: 'Sumber'
            },
            {
            key: 'aplikasi',
            label: 'Aplikasi'
            },
            {
            key: 'post_sample',
            label: 'Post Sample',
            sortable: true
            }
        ],
        item_posts: [],
        item_comments: [],
        neww: [],
        total_post : null,
        total_book: null,
        aplikasi: ''
        }
    },
    async mounted() {
        this.isBusy = true;
        store.state.post.param.access_token = this.$cookie.get('user_token')
        store.state.post.param.user_id = this.$cookie.get('user_id')
        store.state.post.param.startDate = this.$cookie.get('dari_tgl')
        store.state.post.param.endDate = this.$cookie.get('smp_tgl')
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
        styleTable(){
            if(this.$mq === 'desktop'){
                return ""
            }else{
                return "table-wrapper-scroll-y my-custom-scrollbar"
            }
        },
        getImgUrl() {
            var images = require.context("../assets/img/avatar/", false, /\.png$/);
            return images("./" + "avatar-1" + ".png");
        },
        fillData(){
            // let data = store.state.books
            let data_reviews = store.state.post.DataPost
            // for(var i = 0; i < data.length; i++){
            //     if(data[i].created_at > this.neww.dari_tgl && data[i].created_at < this.neww.smp_tgl){
            //         this.total_book += 1
            //         this.items.push({titleimg: {title: data[i].title, cover: data[i].cover}, category: data[i].category, author: data[i].author, publish_date: data[i].publish_date, description: data[i].description})
            //     }
            // }
            for(var i = 0; i < data_reviews.length; i++){
                //store.state.indexx = data_reviews[i].book_id
                // for(var j = 0; j < data.length; j++){
                //if(data_reviews[i].book_id === data[j].id){
                this.total_post += 1
                var post_count = 0
                var negative_count = 0
                var positive_count = 0
                var engagement_count = 0
                for(var j = 0; j < data_reviews.length; j++){
                    if(data_reviews[i].user_name === data_reviews[j].user_name){
                        post_count =+ 1
                        if(data_reviews[j].sentiment === 0){
                            negative_count =+ 1
                            engagement_count -= 5
                        }else if(data_reviews[j].sentiment === 1){
                            positive_count =+ 1
                            engagement_count += 5
                        }
                    }
                    
                }
                if(data_reviews[i].post.length > 50){
                    data_reviews[i].post = data_reviews[i].post.slice(0, 50) + "..."
                }
                //this.items.push({isActive: true, date: data.book.critic_reviews[i].review_date, source: data.book.critic_reviews[i].source, rating: data.book.critic_reviews[i].star_rating, sentiment: data.book.critic_reviews[i].pos_or_neg, post: data.book.critic_reviews[i].snippet, link_review: data.book.critic_reviews[i].review_link,account: { username: this.users[i].name, image: this.users[i].avatar }})
                this.item_comments.push({id: data_reviews[i].id, account: { username: data_reviews[i].user_name, user_avatar: data_reviews[i].user_avatar }, post_sample: data_reviews[i].post, post: post_count, sentiment: { positive: positive_count, negative: negative_count }, engagement: engagement_count, aplikasi: data_reviews[i].aplikasi, sumber: data_reviews[i].sumber})
                this.item_posts.push({id: data_reviews[i].id, account: { username: data_reviews[i].user_name, user_avatar: data_reviews[i].user_avatar }, post: data_reviews[i].post, tanggal_post: data_reviews[i].tanggal_post, sumber: data_reviews[i].sumber, link_review: data_reviews[i].link_review, rating: data_reviews[i].rating, sentiment: data_reviews[i].sentiment, aplikasi: data_reviews[i].aplikasi})
            //}
            }
            this.fillDataChart();
            this.success = true
            this.isLoading = false
        },
        fillDataChart(){
            let data = store.state.post.DataPost
            var positive = 0
            // var neutral = 0
            var negative = 0
            for(var i = 0; i < data.length; i++){
                if(data[i].sentiment === 0){
                    negative += 1
                    this.count += 1
                // }else if(data[i].sentiment === 1){
                //     neutral += 1
                //     this.count += 1
                }else{
                    positive += 1
                    this.count += 1
                }
            }
            this.series[0] = positive
            // this.series[1] = neutral
            this.series[1] = negative
            this.series2[0].data[0] = positive
            // this.series2[0].data[1] = neutral
            this.series2[0].data[1] = negative
            if(this.count !== 0){
                this.success = true 
            }
        },
    },
}
</script>
<style scoped>
    h1 {
        font-size: 100px;
    }
</style>