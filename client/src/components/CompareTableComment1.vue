<template>
    <div>
        <div class="row">
        <div class="col-12 col-md-12 col-lg-12">
        <div class="card">
            <div class="card-header">
                <div>
                    <h4>Post Count by User</h4>
                    <ul class="nav card-header-tabs pull-right"  id="myTab" role="tablist">
                        <li class="nav-item">
                        <a class="nav-link" @click="changeData('Google Play')" data-toggle="tab" href="#" role="tab" aria-controls="home" aria-selected="true"><strong>Google Play</strong></a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" @click="changeData('App Store')" id="profile-tab" data-toggle="tab" href="#" role="tab" aria-controls="profile" aria-selected="false"><strong>App Store</strong></a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" @click="changeData('Instagram')" id="contact-tab" data-toggle="tab" href="#" role="tab" aria-controls="contact" aria-selected="false"><strong>Instagram</strong></a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" @click="changeData('Twitter')" id="contact-tab" data-toggle="tab" href="#" role="tab" aria-controls="contact" aria-selected="false"><strong>Twitter</strong></a>
                        </li>
                    </ul>
                </div>
                </div>
                <div class="card-body">
                <div class="row pb-4">
                    <b-input-group class="col-12 col-lg-12">
                        <b-form-input
                        v-model="filter"
                        type="search"
                        id="filterInput"
                        placeholder="Type to Search"
                        ></b-form-input>
                        <b-input-group-append>
                            <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
                        </b-input-group-append>
                    </b-input-group>
                </div>
                <div class="table-wrapper-scroll-y my-custom-scrollbar text-center" v-if="length !== 0">
                    <b-table striped hover :items="items" :fields="fields" :filter="filter" :filter-included-fields="filterOn" @filtered="onFiltered">
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
                <h4 style="color: red; margin-top: 20px; height: 322px;" class="text-center" v-else>Data tidak ada</h4>
            </div>
            </div>
        </div>
        </div>
    </div>
</template>
<script>
//import axios from 'axios'
import store from '@/store'
export default {
    data() {
        return {
        // Note 'isActive' is left out and will not appear in the rendered table
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
            key: 'engagement',
            label: 'Engagement',
            sortable: true
            },
            {
            key: 'sentiment',
            label: 'Sentiment'
            },
            {
            key: 'post_sample',
            label: 'Post Sample',
            sortable: true
            }
        ],
        items: [],
        length: 0,
        source: 'Google Play',
        aplikasi: '',
        filter: null,
        filterOn: []
        }
    },
    async mounted() {
        this.fillData()
    },
    methods: {
        onFiltered(filteredItems) {
            // Trigger pagination to update the number of buttons/pages due to filtering
            this.totalRows = filteredItems.length
            this.currentPage = 1
        },
        changeData(source){
            this.source = source;
            this.fillData()
        },
        getImgUrl(image) {
            var images = require.context("../assets/img/avatar/", false, /\.png$/);
            return images("./" + image + ".png");
        },
        fillData(){
            this.items = []
            let data = store.state.post.DataCompare1
            for(var i = 0; i < data.length; i++){
                if(data[i].sumber === this.source){
                    var post_count = 0
                    var negative_count = 0
                    var positive_count = 0
                    var engagement_count = 0
                    for(var j = 0; j < data.length; j++){
                        if(data[i].user_name === data[j].user_name){
                            post_count =+ 1
                            if(data[j].sentiment === 0){
                                negative_count =+ 1
                                engagement_count -= 5
                            }else if(data[j].sentiment === 1){
                                positive_count =+ 1
                                engagement_count += 5
                            }
                        }
                        
                    }
                    this.items.push({id: data[i].id, account: { username: data[i].user_name, user_avatar: data[i].user_avatar }, post_sample: data[i].post, post: post_count, sentiment: { positive: positive_count, negative: negative_count }, engagement: engagement_count})
                }
            }
            this.length = this.items.length
        }
    }
}
</script>
<style scoped>
img {
    border-radius: 50%;
}
</style>