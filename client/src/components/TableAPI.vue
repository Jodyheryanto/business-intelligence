<template>
    <div>
        <div class="row">
        <div class="col-12 col-md-12 col-lg-12">
        <div class="card">
            <div class="card-header">
                <div>
                    <h4>API Config</h4>
                </div>
                </div>
                <div class="card-body">
                    <div class="table-wrapper-scroll-y my-custom-scrollbar text-center" v-if="success === true">
                        <b-table striped hover :filter="filter" :filter-included-fields="filterOn" @filtered="onFiltered" :items="items" :fields="fields">
                            <template v-slot:cell(action)="data">
                                <ul type="none">
                                    <li style="display:inline;" class="pr-2"><button style="color: white" @click="data.toggleDetails" class="btn btn-secondary">{{ data.detailsShowing ? 'Hide' : 'Show' }} Details</button></li>
                                    <li style="display:inline;" class="pr-2"><button @click="ubahData(data.item)" class="btn btn-primary">Edit</button></li>
                                </ul>
                            </template>
                            <template #row-details="row">
                                <b-card>
                                    <b-row class="mb-2">
                                        <b-col sm="3" class="text-sm-right"><b>URL API :</b></b-col>
                                        <b-col>{{ row.item.url_api }}</b-col>
                                    </b-row>
                                    <hr>
                                    <b-row class="mb-2">
                                        <b-col sm="3" class="text-sm-right"><b>Parameter 1 :</b></b-col>
                                        <b-col>{{ row.item.param1 }}</b-col>
                                    </b-row>
                                    <hr>
                                    <b-row class="mb-2">
                                        <b-col sm="3" class="text-sm-right"><b>Parameter 2 :</b></b-col>
                                        <b-col>{{ row.item.param2 }}</b-col>
                                    </b-row>
                                    <hr>
                                    <b-row class="mb-2">
                                        <b-col sm="3" class="text-sm-right"><b>Consumer Key :</b></b-col>
                                        <b-col>{{ row.item.consumer_key }}</b-col>
                                    </b-row>
                                    <hr>
                                    <b-row class="mb-2">
                                        <b-col sm="3" class="text-sm-right"><b>Consumer Secret :</b></b-col>
                                        <b-col>{{ row.item.consumer_secret }}</b-col>
                                    </b-row>
                                    <hr>
                                    <b-row class="mb-2">
                                        <b-col sm="3" class="text-sm-right"><b>Access Token :</b></b-col>
                                        <b-col>{{ row.item.access_token }}</b-col>
                                    </b-row>
                                    <hr>
                                    <b-row class="mb-2">
                                        <b-col sm="3" class="text-sm-right"><b>Access Token Secret :</b></b-col>
                                        <b-col>{{ row.item.access_token_secret }}</b-col>
                                    </b-row>
                                    <hr>
                                    <b-button variant="primary" size="sm" class="mr-2" @click="ubahData(row.item)">Edit</b-button>
                                    <b-button size="sm" class="mr-2" @click="row.toggleDetails">Hide Details</b-button>
                                </b-card>
                            </template>
                        </b-table>
                    </div>
                </div>
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
        // Note 'isActive' is left out and will not appear in the rendered table
            fields: [
                {
                key: 'url_api',
                label: 'URL API'
                },
                {
                key: 'param1',
                label: 'Parameter 1'
                },
                {
                key: 'param2',
                label: 'Parameter 2'
                },
                {
                key: 'consumer_key',
                thClass: 'd-none', 
                tdClass: 'd-none'
                },
                {
                key: 'consumer_secret',
                thClass: 'd-none', 
                tdClass: 'd-none'
                },
                {
                key: 'access_token',
                thClass: 'd-none', 
                tdClass: 'd-none'
                },
                {
                key: 'access_token_secret',
                thClass: 'd-none', 
                tdClass: 'd-none'
                },
                {
                key: 'action',
                label: 'Aksi'
                }
            ],
            notificationSystem: {
                options: {
                    success: {
                        position: "topLeft"
                    },
                    warning: {
                        position: "topLeft"
                    },
                }
            },
            form: {
                is_active: null,
            },
            items: [],
            success: false,
            myRole: null,
            filter: null,
            filterOn: []
        }
    },
    async mounted() {
        this.isBusy = true;
        this.myRole = this.$cookie.get('user_role')
        store.state.post.param.access_token = this.$cookie.get('user_token')
        try {
            await this.$store.dispatch('api/getApi')
            this.fillData()
        } catch (ex) {
            this.error = "Failed to load data";
        } finally {
            this.isBusy = false;
        }
    },
    methods: {
        onFiltered(filteredItems) {
            // Trigger pagination to update the number of buttons/pages due to filtering
            this.totalRows = filteredItems.length
            this.currentPage = 1
        },
        fillData(){
            let data = store.state.api.apiconfig
            for(var i = 0; i < data.length; i++){
                this.items.push({id: data[i].id, url_api: data[i].url_api, param1: data[i].param1, param2: data[i].param2, consumer_key: data[i].consumer_key, consumer_secret: data[i].consumer_secret, access_token: data[i].access_token, access_token_secret: data[i].access_token_secret})
            }
            this.success = true
        },
        ubahData(item){
            this.$eventBus.$emit("datafromtableAPI", item);
            this.$modal.show("modal-ubah-api");
        }
    }
}
</script>