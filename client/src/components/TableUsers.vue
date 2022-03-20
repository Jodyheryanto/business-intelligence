<template>
    <div>
        <loading :active.sync="isLoading" 
            :is-full-page="fullPage"></loading>
        <div class="row">
        <div class="col-12 col-md-12 col-lg-12">
        <div class="card">
            <div class="card-header">
                <div>
                    <h4>Users</h4>
                </div>
                </div>
                <div class="card-body">
                <div class="row pb-4">
                    <div class="col"></div>
                    <b-input-group class="col-12 col-lg-4 float-right">
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
                <div class="table-wrapper-scroll-y my-custom-scrollbar text-center" v-if="success === true">
                    <b-table striped hover :filter="filter" :filter-included-fields="filterOn" @filtered="onFiltered" :items="items" :fields="fields">
                        <template v-slot:cell(is_active)="data">
                            <ul type="none" v-if="data.value === -1" style="margin: 0; margin-top: 5px">
                                <li><a style="color: white" class="badge badge-danger">Rejected</a></li>
                            </ul>
                            <ul type="none" v-if="data.value === 0" style="margin: 0; margin-top: 5px">
                                <li style="display:inline;" class="pr-2"><button style="color: white" @click="data.toggleDetails" class="btn btn-secondary">{{ data.detailsShowing ? 'Hide' : 'Show' }} Details</button></li>
                                <li style="display:inline;" class="pr-2"><button @click="ubahAccepted(data.item)" class="btn btn-success">Accept</button></li>
                                <li style="display:inline;"><button @click="ubahRejected(data.item)" class="btn btn-danger">Reject</button></li>
                            </ul>
                            <ul type="none" v-if="data.value === 1" style="margin: 0; margin-top: 5px">
                                <li style="display:inline;" class="pr-2"><button style="color: white" @click="data.toggleDetails" class="btn btn-secondary">{{ data.detailsShowing ? 'Hide' : 'Show' }} Details</button></li>
                                <li style="display:inline;" class="pr-2"><button @click="ubahData(data.item)" class="btn btn-primary">Edit</button></li>
                                <!-- <li style="display:inline;"><a href="#" @click="deleteData(data.item.id)" class="badge badge-warning">Delete</a></li> -->
                            </ul>
                            <ul type="none" v-if="data.value === 2" style="margin: 0; margin-top: 5px">
                                <li><a style="color: white" class="badge badge-danger">You Can't Do Anything</a></li>
                            </ul>
                        </template>
                        <template #row-details="row">
                            <b-card>
                                <b-row class="mb-2">
                                    <b-col sm="3" class="text-sm-right"><b>Name :</b></b-col>
                                    <b-col>{{ row.item.name }}</b-col>
                                </b-row>
                                <hr>
                                <b-row class="mb-2">
                                    <b-col sm="3" class="text-sm-right"><b>Email :</b></b-col>
                                    <b-col>{{ row.item.email }}</b-col>
                                </b-row>
                                <hr>
                                <b-row class="mb-2">
                                    <b-col sm="3" class="text-sm-right"><b>Nama Aplikasi :</b></b-col>
                                    <b-col>{{ row.item.nama_aplikasi }}</b-col>
                                </b-row>
                                <hr>
                                <b-row class="mb-2">
                                    <b-col sm="3" class="text-sm-right"><b>ID in Google Play :</b></b-col>
                                    <b-col>{{ row.item.app_google_play }}</b-col>
                                </b-row>
                                <hr>
                                <b-row class="mb-2">
                                    <b-col sm="3" class="text-sm-right"><b>ID in App Store :</b></b-col>
                                    <b-col>{{ row.item.app_apps_store }}</b-col>
                                </b-row>
                                <hr>
                                <b-row class="mb-2">
                                    <b-col sm="3" class="text-sm-right"><b>Keyword in Instagram :</b></b-col>
                                    <b-col>{{ row.item.keyword_ig }}</b-col>
                                </b-row>
                                <hr>
                                <b-row class="mb-2">
                                    <b-col sm="3" class="text-sm-right"><b>Keyword in Twitter :</b></b-col>
                                    <b-col>{{ row.item.keyword_twitter }}</b-col>
                                </b-row>
                                <hr>
                                <b-row class="mb-2">
                                    <b-col sm="3" class="text-sm-right"><b>Description :</b></b-col>
                                    <b-col>{{ row.item.description }}</b-col>
                                </b-row>
                                <hr>
                                <b-row class="mb-2">
                                    <b-col sm="3" class="text-sm-right"><b>Status :</b></b-col>
                                    <b-col>
                                        <p class="badge badge-success" v-if="row.item.is_active === 1"> Active </p>
                                        <p class="badge badge-warning" v-else-if="row.item.is_active === 0"> In Process </p>
                                        <p class="badge badge-danger" v-else-if="row.item.is_active === -1"> Rejected </p>
                                        <p class="badge badge-danger" v-else-if="row.item.is_active"> Admin </p>
                                    </b-col>
                                </b-row>
                                <hr>
                                <b-button variant="success" size="sm" class="mr-2" v-if="row.item.is_active === 0" @click="ubahAccepted(row.item)">Accept</b-button>
                                <b-button variant="danger" size="sm" class="mr-2" v-if="row.item.is_active === 0" @click="ubahRejected(row.item)">Reject</b-button>
                                <b-button variant="primary" size="sm" class="mr-2" v-if="row.item.is_active === 1" @click="ubahData(row.item)">Edit</b-button>
                                <b-button variant="danger" size="sm" class="mr-2" v-if="row.item.is_active === 1" @click="deleteData(row.item.id)">Delete</b-button>
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
import { mapActions } from 'vuex'
import store from '@/store'
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/vue-loading.css';
export default {
    components: {
        Loading
    },
    data() {
        return {
        // Note 'isActive' is left out and will not appear in the rendered table
            fields: [
                {
                key: 'name',
                label: 'Name',
                sortable: true
                },
                {
                key: 'email',
                label: 'Email',
                sortable: true
                },
                // {
                // key: 'phone_no',
                // label: 'Number Phone',
                // sortable: true
                // },
                {
                key: 'nama_aplikasi',
                label: 'Nama Aplikasi',
                sortable: true
                },
                {
                key: 'app_google_play',
                thClass: 'd-none', 
                tdClass: 'd-none'
                },
                {
                key: 'app_apps_store',
                thClass: 'd-none', 
                tdClass: 'd-none'
                },
                {
                key: 'keyword_ig',
                thClass: 'd-none', 
                tdClass: 'd-none'
                },
                {
                key: 'keyword_twitter',
                thClass: 'd-none', 
                tdClass: 'd-none'
                },
                {
                key: 'description',
                label: 'Deskripsi (Tambahan/Permintaan)',
                sortable: true
                },
                {
                key: 'is_active',
                label: 'Actions'
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
            filterOn: [],
            isLoading: false,
            fullPage: true
        }
    },
    async mounted() {
        this.isBusy = true;
        this.myRole = this.$cookie.get('user_role')
        store.state.post.param.access_token = this.$cookie.get('user_token')
        try {
            await this.$store.dispatch('auth/getUsers')
            this.fillData()
        } catch (ex) {
            this.error = "Failed to load data";
        } finally {
            this.isBusy = false;
        }
    },
    methods: {
        ...mapActions({
            ubahStatus: 'auth/ubahStatus'
        }),
        onFiltered(filteredItems) {
            // Trigger pagination to update the number of buttons/pages due to filtering
            this.totalRows = filteredItems.length
            this.currentPage = 1
        },
        ubahAccepted(item){
            this.isLoading = true
            store.state.auth.user_id = item.id
            this.form.is_active = 1
            store.state.auth.is_active = this.form
            this.ubahStatus().then(() => {
                if(store.state.auth.successUbah === true){
                    this.isLoading = false
                    this.$toast.success('You change the status!', 'Success', this.notificationSystem.options.success)
                    setTimeout( () => location.reload(), 3000)
                }else{
                    this.isLoading = false
                    this.$toast.warning("I don't know, just error I guess?", 'Failed', this.notificationSystem.options.warning)
                }
            })
        },
        ubahRejected(item){
            this.isLoading = true
            store.state.auth.user_id = item.id
            this.form.is_active = -1
            store.state.auth.is_active = this.form
            this.ubahStatus().then(() => {
                if(store.state.auth.successUbah === true){
                    this.isLoading = false
                    this.$toast.success('You change the status!', 'Success', this.notificationSystem.options.success)
                    setTimeout( () => location.reload(), 3000)
                }else{
                    this.isLoading = false
                    this.$toast.warning("I don't know, just error I guess?", 'Failed', this.notificationSystem.options.warning)
                }
            })
        },
        fillData(){
            let data = store.state.auth.data_user
            for(var i = 0; i < data.length; i++){
                if(data[i].is_active === 2){
                    this.items.push({id: data[i].id, name: data[i].name, email: data[i].email, app_google_play: data[i].app_google_play, app_apps_store: data[i].app_apps_store, keyword_ig: data[i].keyword_ig, keyword_twitter: data[i].keyword_twitter, description: data[i].description, nama_aplikasi: data[i].nama_aplikasi, is_active: data[i].is_active})
                }else{
                    this.items.push({id: data[i].id, name: data[i].name, email: data[i].email, app_google_play: data[i].app_google_play, app_apps_store: data[i].app_apps_store, keyword_ig: data[i].keyword_ig, keyword_twitter: data[i].keyword_twitter, description: data[i].description, nama_aplikasi: data[i].nama_aplikasi, is_active: data[i].is_active})
                }
            }
            this.success = true
        },
        ubahData(item){
            this.$eventBus.$emit("datafromtableUser", item);
            this.$modal.show("modal-ubah");
        },
        async deleteData(item){
            var r = confirm("Are you sure about that ?");
            if (r == true) {
                store.state.auth.user_id = item
                this.isBusy = true;
                try {
                    await this.$store.dispatch('auth/delete')
                    if(store.state.auth.successDelete === true){
                        this.$toast.success('You delete the data!', 'Success', this.notificationSystem.options.success)
                        setTimeout( () => location.reload(), 3000)
                    }else{
                        this.$toast.warning("I don't know, just error I guess?", 'Failed', this.notificationSystem.options.warning)
                    }
                } catch (ex) {
                    this.error = "Failed to load data";
                } finally {
                    this.isBusy = false;
                }
            }
        }
    }
}
</script>