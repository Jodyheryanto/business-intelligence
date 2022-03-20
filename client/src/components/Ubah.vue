<template>
  <modal 
    name="modal-ubah"
    transition="nice-modal-fade"
    height="auto" 
    :scrollable="true"
    :delay="100"
    :adaptive="true">
  <loading :active.sync="isLoading" 
      :is-full-page="fullPage"></loading>
  <div class="example-modal-content">
      <h3 style="margin: 15px 20px;">Form Ubah Data</h3>
      <hr>
      <p v-if="errors.length" style="margin-left: 25px;">
          <b>Please correct the following error(s):</b>
          <b v-for="(error,index) in errors" v-bind:key="index" style="color: red;"> {{ error }},</b><b style="color: red;"> Required</b>
      </p>
      <br>
      <ul type="none">
          <li>
              <div class="form-group" style="margin-top: -20px;">
                <label for="judul">Name : </label>
                <input type="text" class="form-control" name="judul" style="width: 90%;" v-model="form.name" required>
              </div>
          </li>
          <li>
              <div class="form-group mb-0" style="margin-top: -20px;">
                <label for="deskripsi">Email : </label>
                <input type="email" class="form-control" name="deskripsi" style="width: 90%;" v-model="form.email" required>
              </div>
          </li>
          <li>
              <div class="form-group">
                <label for="judul">Nama Aplikasi : </label>
                <input type="text" class="form-control" name="judul" style="width: 90%;" placeholder="ex: ai.lenna.assistant" v-model="form.nama_aplikasi" disabled>
              </div>
          </li>
          <li>
              <div class="form-group">
                <label for="judul">Your Name Apps (Google Play) : </label>
                <input type="text" class="form-control" name="judul" style="width: 90%;" placeholder="ex: ai.lenna.assistant" v-model="form.app_google_play" disabled>
              </div>
          </li>
          <li>
              <div class="form-group" style="margin-top: -20px;">
                <label for="judul">Your Name Apps (Apps Store) : </label>
                <input type="text" class="form-control" name="judul" placeholder="ex: ai.lenna.assistant" style="width: 90%;" v-model="form.app_apps_store" disabled>
              </div>
          </li>
          <li>
              <div class="form-group" style="margin-top: -20px;">
                <label for="judul">Keyword for Instagram : </label>
                #<input type="text" class="form-control" name="judul" placeholder="ex: lennaassistant" style="width: 90%;" v-model="form.keyword_ig" disabled>
              </div>
          </li>
          <li>
              <div class="form-group" style="margin-top: -20px;">
                <label for="judul">Keyword for Twitter : </label>
                #<input type="text" class="form-control" name="judul" placeholder="ex: lennaassistant" style="width: 90%;" v-model="form.keyword_twitter" disabled>
              </div>
          </li>
          <li>
              <div class="form-group" style="margin-top: -20px;">
                <label for="judul">Status : </label>
                <input type="text" class="form-control" name="judul" placeholder="ex: ai.lenna.assistant" style="width: 90%;" v-model="form.is_active">
              </div>
          </li>
          <li>
              <div class="form-group" style="margin-top: -20px;">
                <div class="custom-control custom-checkbox">
                  <input type="checkbox" name="agree" class="custom-control-input" id="agree" v-model="isAgree">
                  <label class="custom-control-label" for="agree">I agree with the terms and conditions</label>
                </div>
              </div>
          </li>
      </ul>
      <footer class="modal-footer" style="margin-top: -40px">
        <slot name="footer">
          <button v-on:click="submitForm" class="btn-blue" style="margin: -3px 30px; padding: 10px;">Ubah Data</button>
        </slot>
      </footer>
  </div>
</modal>
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
        form: {
            name: '',
            email: '',
            nama_aplikasi: '',
            app_google_play: '',
            app_apps_store: '',
            keyword_ig: '',
            keyword_twitter: '',
            description: '',
            is_active: null,
        },
        changePass : false,
        errors:[],
        password_confirmation: '',
        isAgree: false,
        notificationSystem: {
          options: {
              success: {
                  position: "topLeft"
              },
              warning: {
                  position: "topLeft"
              },
          }
        }
      }
  },
  mounted() {
    this.$eventBus.$on("datafromtableUser", (x) => {
      this.neww = x;
      this.form.name = this.neww.name
      this.form.email = this.neww.email
      this.form.nama_aplikasi = this.neww.nama_aplikasi
      this.form.app_google_play = this.neww.app_google_play
      this.form.app_apps_store = this.neww.app_apps_store
      this.form.keyword_ig = this.neww.keyword_ig
      this.form.keyword_twitter = this.neww.keyword_twitter
      this.form.description = this.neww.description
      this.form.is_active = this.neww.is_active
      store.state.auth.user_id = this.neww.id
    });
  },
  methods:{
      ...mapActions({
        ubah: 'auth/ubah'
      }),
      changeStats(){
        if (!this.changePass) this.changePass = true; else this.changePass = false
      },
      async submitForm(e){
          this.isLoading = true
          if(this.isAgree){
            if(this.form.name && this.form.email && this.form.app_google_play && this.form.app_apps_store && this.form.keyword_ig && this.form.keyword_twitter && this.form.is_active){
              store.state.auth.param_user = this.form
              this.ubah().then(() => {
                if(store.state.auth.successUbah === true){
                  this.isLoading = false
                  this.$toast.success('You change the data!', 'Success', this.notificationSystem.options.success)
                  setTimeout( () => location.reload(), 3000)
                }else{
                  this.isLoading = false
                  this.$toast.warning("I don't know, just error I guess?", 'Failed', this.notificationSystem.options.warning)
                }
              })
            }
            this.errors = [];
            if(!this.form.name) this.errors.push("Name");
            if(!this.form.email) this.errors.push("Email");
            if(!this.form.app_google_play) this.errors.push("Your Name Apps (Google Play)");
            if(!this.form.app_apps_store) this.errors.push("Your Name Apps (Apps Store)");
            if(!this.form.keyword_ig) this.errors.push("Keyword for Instagram");
            if(!this.form.keyword_twitter) this.errors.push("Keyword for Twitter");
            if(!this.form.is_active) this.errors.push("Status");
            e.preventDefault();
          }else{
            this.isLoading = false
            this.$toast.warning('You must be agree for terms and condition', 'Failed', this.notificationSystem.options.warning)
          }
      }
  }
}
</script>

<style scope>
.v--modal-box {
  margin: 10px;
}
</style>