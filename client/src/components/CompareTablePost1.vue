<template>
    <div>
        <div class="row">
        <div class="col-12 col-md-12 col-lg-12">
        <div class="card">
            <div class="card-header">
                <div>
                    <h4>Posts</h4>
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
                    <b-input-group class="col-12 col-lg-12 float-right">
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
                        <template v-slot:cell(sumber)="data">
                            <a :href="items[data.index].link_review" target="_blank">{{ data.value }}</a>
                        </template>
                        <template v-slot:cell(sentiment)="data">
                            <div v-if="data.value === 0">
                                <p class="badge badge-danger">negative</p>
                            </div>
                            <div v-if="data.value === 1">
                                <p class="badge badge-success">positive</p>
                            </div>
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
import store from '@/store'
import moment from 'moment'
export default {
    data() {
        return {
        // Note 'isActive' is left out and will not appear in the rendered table
        success: false,
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
            key: 'rating',
            label: 'Rating',
            sortable: true
            },
            {
            key: 'sentiment',
            label: 'Sentiment'
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
                    this.items.push({id: data[i].id, account: { username: data[i].user_name, user_avatar: data[i].user_avatar }, post: data[i].post, tanggal_post: moment(data[i].tanggal_post).format('DD MMM YYYY'), sumber: data[i].sumber, link_review: data[i].link_review, rating: data[i].rating, sentiment: data[i].sentiment})
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
