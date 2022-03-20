<template>
    <div>
        <loading :active.sync="isLoading" 
            :is-full-page="fullPage"></loading>
        <div class="row">
        <div class="col-12 col-md-12 col-lg-12">
        <div class="card">
            <div class="card-header">
                <div>
                    <h4>Data Help Users</h4>
                </div>
                </div>
                <div class="card-body">
                <div class="row pb-4">
                    <div class="col"></div>
                    <button @click="createHelp()" class="btn btn-success">Create</button>
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
                        <template v-slot:cell(id)="data">
                            <ul type="none" style="margin: 0; margin-top: 5px">
                                <li style="display:inline;" class="pr-2"><button @click="ubahData(data.item)" class="btn btn-primary">Edit</button></li>
                                <li style="display:inline;"><a href="#" @click="deleteData(data.item.id)" class="btn btn-warning">Delete</a></li>
                            </ul>
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
            isLoading: false,
            fullPage: true,
            fields: [
                {
                key: 'title',
                label: 'Judul',
                sortable: true
                },
                {
                key: 'description',
                label: 'Deskripsi',
                sortable: true
                },
                {
                key: 'id',
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
            filterOn: []
        }
    },
    async mounted() {
        this.isBusy = true;
        store.state.help.param.access_token = this.$cookie.get('user_token')
        this.name = this.$cookie.get('user_name')
        this.role = parseInt(this.$cookie.get('user_role'))
        try {
            await this.$store.dispatch('help/loadDataHelp')
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
        createHelp(){
            this.$modal.show("modal-tambah-help");
        },
        fillData(){
            let data = store.state.help.DataHelp
            for(var i = 0; i < data.length; i++){
                this.items.push({id: data[i].id, title: data[i].title, description: data[i].description})
            }
            this.success = true
        },
        ubahData(item){
            this.$eventBus.$emit("datafromtableHelp", item);
            this.$modal.show("modal-ubah-help");
        },
        async deleteData(item){
            var r = confirm("Are you sure about that ?");
            if (r == true) {
                this.isLoading = true
                store.state.help.param.id = item
                store.state.help.param.access_token = this.$cookie.get('user_token')
                this.isBusy = true;
                try {
                    await this.$store.dispatch('help/delete')
                    if(store.state.help.help.status == 200){
                        this.isLoading = false
                        this.$toast.success(store.state.help.help.data.message, 'Success', this.notificationSystem.options.success)
                        setTimeout( () => location.reload(), 3000)
                    }else{
                        this.isLoading = false
                        this.$toast.warning(store.state.help.help.data.message, 'Failed', this.notificationSystem.options.warning)
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