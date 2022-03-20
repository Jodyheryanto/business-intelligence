<template>
  <fixed-header>
    <div class="navbar vue-fixed-header--isFixed">
      <div class="navbar-bg"></div>
        <nav class="navbar navbar-expand-lg main-navbar">
          <a href="#" @click="Home" class="navbar-brand sidebar-gone-hide">
          <!-- <img height="50px" src="../assets/logo.png" alt="logo"> --><h1>LOGO</h1></a> 
          <a href="#" class="nav-link sidebar-gone-show" @click="toggleBodyClassMini(kondisiMini, 'sidebar-gone')" data-toggle="sidebar"><i class="fas fa-bars"></i></a>
          <div class="nav-collapse">
            <ul class="navbar-nav">
              <li class="nav-item active"><a @click="Home" href="#" class="nav-link">Home</a></li>
              <li class="nav-item" v-if="role === 1"><a @click="CompareReviews" href="#" class="nav-link">Compare Reviews</a></li>
              <li class="nav-item" v-if="role === 2"><a @click="UsersData" href="#" class="nav-link">Users Data</a></li>
              <li class="nav-item" v-if="role === 2"><a @click="APIConfig" href="#" class="nav-link">API Config</a></li>
              <li class="nav-item" v-if="role === 2"><a @click="ReviewsData" href="#" class="nav-link">Reviews Data</a></li>
              <li class="nav-item" v-if="role === 2"><a @click="SupportUser" href="#" class="nav-link">Support User</a></li>
              <li class="nav-item"><a @click="ReportReviews" href="#" class="nav-link">Report Reviews</a></li>
            </ul>
            <b-nav pills v-if="$mq === 'mobile' || $mq === 'tablet'" style="background-color: #f6f7fe; margin-top: -10px">
                <b-nav-item-dropdown
                text="Menu"
                toggle-class="nav-link-custom"
                right
                >
                  <b-dropdown-item><a @click="Home" href="" class="nav-link">Home</a></b-dropdown-item>
                  <b-dropdown-item v-if="role === 1"><a @click="CompareReviews" href="#" class="nav-link">Compare Reviews</a></b-dropdown-item>
                  <b-dropdown-item v-if="role === 2"><a @click="UsersData" href="#" class="nav-link">Users Data</a></b-dropdown-item>
                  <b-dropdown-item v-if="role === 2"><a @click="APIConfig" href="#" class="nav-link">API Config</a></b-dropdown-item>
                  <b-dropdown-item v-if="role === 2"><a @click="ReviewsData" href="#" class="nav-link">Reviews Data</a></b-dropdown-item>
                  <b-dropdown-item v-if="role === 2"><a @click="SupportUser" href="#" class="nav-link">Support User</a></b-dropdown-item>
                  <b-dropdown-item><a @click="ReportReviews" href="#" class="nav-link">Report Reviews</a></b-dropdown-item>
                </b-nav-item-dropdown>
            </b-nav>
          </div>
          <form class="form-inline ml-auto">
            <!-- <ul class="navbar-nav">
              <li><a href="#" data-toggle="search" class="nav-link nav-link-lg d-sm-none"><i class="fas fa-search"></i></a></li>
            </ul>
            <div class="search-element">
              <input class="form-control" type="search" placeholder="Search" aria-label="Search" data-width="250">
              <button class="btn" type="submit"><i class="fas fa-search"></i></button>
            </div> -->
          </form>
          <ul class="navbar-nav navbar-right">
            <li class="dropdown dropdown-list-toggle">
              <a href="#" v-if="notRead > 0" data-toggle="dropdown" class="nav-link notification-toggle nav-link-lg beep">
                <i class="far fa-bell"></i>
              </a>
              <a href="#" v-else data-toggle="dropdown" class="nav-link notification-toggle nav-link-lg">
                <i class="far fa-bell"></i>
              </a>
              <div class="dropdown-menu dropdown-list dropdown-menu-right">
                <div class="dropdown-header">Notifications
                </div>
                <div class="dropdown-list-content dropdown-list-icons" v-if="successvar == true">
                  <div v-for="(data, index) in DataNotif" v-bind:key="index">
                    <a href="#" v-b-modal="'modal-' + data.id" @click="ubahStatNotif(data)" :class="data.style" >
                      <div class="dropdown-item-icon bg-primary text-white">
                        <i class="fas fa-code"></i>
                      </div>
                      <div class="dropdown-item-desc">
                        {{ data.title }}
                        <div class="time text-primary">{{ data.tanggal_notif }}</div>
                      </div>
                    </a>
                    <b-modal :id="'modal-' + data.id" :title="data.title">
                        <p class="my-4" v-html="data.description"></p>
                    </b-modal>
                  </div>
                  <div v-if="DataNotif.length == 0">Tidak ada notifikasi</div>
                </div>
              </div>
            </li>
            <li class="dropdown dropdown-list-toggle"><a href="#" data-toggle="dropdown" class="nav-link nav-link-lg message-toggle"><i class="fas fa-question-circle"></i></a>
              <div class="dropdown-menu dropdown-list dropdown-menu-right">
                <!-- <div class="dropdown-header">
                  <div class="input-group">
                    <div class="input-group-prepend">
                      <div class="input-group-text">
                        <i class="fas fa-search"></i>
                      </div>
                    </div>
                    <input type="text" class="form-control phone-number">
                  </div>
                </div> -->
                <div class="dropdown-list-icons">
                  <div class="card">
                    <div class="card-header pt-0 pb-0 mt-0 mb-0">
                      <strong>Need Helps ?</strong>
                    </div>
                    <div class="card-body pt-0 pb-0 mt-1 mb-0">
                      <a href="#" @click="HelpUsers()" class="dropdown-item">
                        <div class="dropdown-item-icon bg-info text-white">
                          <i class="fas fa-comments"></i>
                        </div>
                        <div class="dropdown-item-desc">
                          Check FAQ List
                          <div class="text-primary">List Question and Answer from Users.</div>
                        </div>
                      </a>
                      <a href="https://mail.google.com/mail/?view=cm&fs=1&to=info@lenna.ai" target="_blank" class="dropdown-item">
                        <div class="dropdown-item-icon bg-info text-white">
                          <i class="fas fa-headset"></i>
                        </div>
                        <div class="dropdown-item-desc">
                          Contact us
                          <div class="text-primary">Tell us more and we’ll help you.</div>
                        </div>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </li>
            <li class="dropdown"><a href="#" data-toggle="dropdown" class="nav-link dropdown-toggle nav-link-lg nav-link-user">
              <img alt="image" src="../assets/img/avatar/avatar-1.png" class="rounded-circle mr-1">
              <!-- <avatar :username="name" class="rounded-circle vertical-align: middle; mr-1"></avatar> -->
              <div class="d-sm-none d-lg-inline-block" style="text-transform: capitalize">Hi, <template v-if="success">{{ name }}</template></div></a>
              <div class="dropdown-menu dropdown-menu-right">
                <a href="features-profile.html" class="dropdown-item has-icon">
                  <i class="far fa-user"></i> Profile
                </a>
                <a href="#" v-b-modal.modal-ubah class="dropdown-item has-icon">
                  <i class="fas fa-key"></i> Change Password
                </a>
                <div class="dropdown-divider"></div>
                <a href="#" @click.prevent="signOut" class="dropdown-item has-icon text-danger">
                  <i class="fas fa-sign-out-alt"></i> Logout
                </a>  
                <loading :active.sync="isLoading" 
                  :is-full-page="fullPage"></loading>
                <b-modal id="modal-ubah" title="Change Password">
                    <b-container fluid>
                      <p v-if="errors.length" style="margin-left: 25px;">
                          <b>Please correct the following error(s):</b>
                          <b v-for="(error,index) in errors" v-bind:key="index" style="color: red;"> {{ error }},</b><b style="color: red;"> Required</b>
                      </p>
                      <br>
                      <ul type="none">
                        <li>
                            <div class="form-group">
                              <label for="deskripsi">Password : </label>
                              <input type="password" class="form-control" placeholder="Please fill this password for confirmation" style="width: 90%;" v-model="form.password">
                            </div>
                        </li>
                        <li>
                            <div class="form-group">
                              <label for="judul">New Password : </label>
                              <input type="password" class="form-control" style="width: 90%;" placeholder="Please fill new password" v-model="form.new_password">
                            </div>
                        </li>
                        <li>
                            <div class="form-group">
                              <label for="judul">Retype New Password : </label>
                              <input type="password" class="form-control" style="width: 90%;" placeholder="Please retype new password" v-model="form.renew_password">
                            </div>
                        </li>
                      </ul>
                    </b-container>
                    <template #modal-footer>
                      <div class="w-100">
                        <b-button
                          variant="danger"
                          class="float-right ml-2"
                          @click="show=false"
                        >
                          Close
                        </b-button>
                        <b-button
                          variant="primary"
                          class="float-right"
                          @click="ubahPassword()"
                        >
                          Change
                        </b-button>
                      </div>
                    </template>
                </b-modal>
              </div>
            </li>
          </ul>
        </nav>
  </div>
  </fixed-header>
</template>
<script>
import { mapActions } from 'vuex'
import FixedHeader from 'vue-fixed-header'
// import Avatar from 'vue-avatar'
import store from '@/store'
// Import component
import Loading from 'vue-loading-overlay';
// Import stylesheet
import 'vue-loading-overlay/dist/vue-loading.css';
export default {
  components: {
    FixedHeader,
    Loading
  },
  data(){
    return{
      notificationSystem: {
        options: {
          success: {
              position: "topLeft"
          },
          warning: {
              position: "topLeft"
          },
        },
      },
      form: {
        password: '',
        new_password: '',
        renew_password: '',
      },
      label_menus: [],
      DataNotif: [],
      kondisiMini: false,
      name: "",
      role: null,
      successvar: false,
      isLoading: false,
      fullPage: true,
      notRead: 0,
      errors: []
    }
  },
  computed: {
      success(){
        return eval(this.$cookie.get('user_success'))
      }
  },
  async mounted() {
    this.isBusy = true;
    store.state.notification.param.user_id = this.$cookie.get('user_id')
    store.state.notification.param.preview = true
    store.state.notification.param.access_token = this.$cookie.get('user_token')
    this.name = this.$cookie.get('user_name')
    this.role = parseInt(this.$cookie.get('user_role'))
    try {
        await this.$store.dispatch('notification/loadDataNotif')
        this.fillData()
    } catch (ex) {
        this.error = "Failed to load data";
    } finally {
        this.isBusy = false;
    }
  },
  methods: {
    ...mapActions({
      ubahPasswordAct: 'auth/ubahPassword'
    }),
    async ubahPassword(){
      if(this.form.password && this.form.new_password && this.form.renew_password){
        this.isLoading = true
        if(this.form.password != this.form.new_password){
          if(this.form.new_password == this.form.renew_password){
            store.state.auth.param_password = this.form
            store.state.auth.user_id = this.$cookie.get('user_id')
            store.state.post.param.access_token = this.$cookie.get('user_token')
            this.ubahPasswordAct().then(() => {
              if(store.state.auth.UbahPass.status == 200){
                this.isLoading = false
                this.$toast.success(store.state.auth.UbahPass.data.message, 'Success', this.notificationSystem.options.success)
                setTimeout( () => location.reload(), 3000)
              }else{
                this.isLoading = false
                this.$toast.warning(store.state.auth.UbahPass.data.message, 'Failed', this.notificationSystem.options.warning)
              }
            })
          }else{
            this.isLoading = false
                this.$toast.warning("Retype new password does not match !", 'Failed', this.notificationSystem.options.warning)
          }
        }else{
          this.isLoading = false
          this.$toast.warning("Your new password as same as old password !", 'Failed', this.notificationSystem.options.warning)
        }
      }
      this.errors = [];
      if(!this.form.new_password) this.errors.push("New Password");
      if(!this.form.renew_password) this.errors.push("Retype New Password");
      if(!this.form.password) this.errors.push("Password");
    },
    async ubahStatNotif(data){
      store.state.notification.param.id = data.id
      if(data.status == 0){
        this.notRead = this.notRead - 1
        this.DataNotif[this.DataNotif.indexOf(data)].style = 'dropdown-item dropdown-item-read'
        await this.$store.dispatch('notification/ubahStatusNotif')
      }
    },
    fillData(){
        // let data = store.state.post.DataPost.data
        let data = store.state.notification.DataNotif
        if(data.length > 5){
          var length = 5
        }else{
          length = data.length
        }
        for(var i = 0; i < length; i++){
            if(data[i].status == 0){
              this.notRead = this.notRead + 1
              var varStyle = 'dropdown-item dropdown-item-unread'
            }else{
              varStyle = 'dropdown-item dropdown-item-read'
            }
            this.DataNotif.push({id: data[i].id, status: data[i].status, tanggal_notif: data[i].tanggal_notif, title: data[i].title, description: data[i].description, style: varStyle})
        }
        this.successvar = true
        this.isLoading = false;
    },
    fillDataMenu(){
        let response = store.state.menu.data_menu
        for(var i = 0; i < response.data.length; i++){
            this.label_menus.push(response.data[i].name)
        }
    },
    toggleBodyClassMini(kondisi, className) {
        const el = document.body;

        if (kondisi === true) {
            el.classList.add(className);
        } else {
            el.classList.remove(className);
        }
    },
    ...mapActions({
        signOutAction: 'auth/signOut'
    }),
    Home(){
        this.$router.replace({
            name: 'Home'
        })
        location.reload()
    },
    ReportReviews(){
        // this.$router.replace({
        //     name: 'ReportBooks'
        // })
        this.$modal.show('filter-data');
    },
    CompareReviews(){
        // this.$router.replace({
        //     name: 'ReportBooks'
        // })
        this.$modal.show('versus-date');
    },
    UsersData(){
        this.$router.replace({
            name: 'UsersData'
        })
        location.reload()
    },
    APIConfig(){
        this.$router.replace({
            name: 'APIConfig'
        })
        location.reload()
    },
    ReviewsData(){
        this.$router.replace({
            name: 'ReviewsData'
        })
        location.reload()
    },
    HelpUsers(){
        this.$router.replace({
            name: 'QAUsers'
        })
        location.reload()
    },
    SupportUser(){
        this.$router.replace({
            name: 'SupportUser'
        })
        location.reload()
    },
    signOut(){
        var r = confirm("Are you sure about that ?");
        if (r == true) {
          this.signOutAction()
          this.$cookie.set('filterClick', false);
          this.$cookie.set('startDate', null);
          this.$cookie.set('endDate', null);
          this.$cookie.set('user_success', null);
          this.$cookie.set('user_name', null);
          this.$cookie.set('user_role', null);
          this.$cookie.set('user_googleplay', null);
          this.$cookie.set('user_appstore', null);
          this.$cookie.set('user_twitter', null);
          this.$cookie.set('user_instagram', null);
          this.$cookie.set('user_nama_aplikasi', null);
          this.$cookie.set('user_token', null);
          for(var i=0; i<2; i++){
              this.$cookie.set('sentiment'+i, null)
          }
          for(i=0; i<4; i++){
              this.$cookie.set('source'+i, null)
          }
          this.$toast.success('You Succeeded Logout!', 'Congratulation', this.notificationSystem.options.success)
          setTimeout( () => this.$router.replace({
              name: 'Auth'
          }), 2000)
        }
    }
  },
}
</script>
<style>
.vue-fixed-header--isFixed {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
}
</style> 