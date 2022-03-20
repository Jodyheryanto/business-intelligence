<template>
  <modal 
    name="example-adaptive"
    transition="nice-modal-fade"
    height="auto" 
    :scrollable="true"
    :delay="100"
    :adaptive="true">
    <loading :active.sync="isLoading" 
            :is-full-page="fullPage"></loading>
  <div class="example-modal-content">
      <h3 style="margin: 15px 20px;">Form Registrasi</h3>
      <hr>
      <p v-if="errors.length" style="margin-left: 25px;">
          <b>Please correct the following error(s):</b>
          <b v-for="(error,index) in errors" v-bind:key="index" style="color: red;"> {{ error }},</b><b style="color: red;"> Required</b>
      </p>
      <br>
      <ul type="none">
          <li>
              <div class="form-group" style="margin-top: -20px;">
                <label>Name<span style="color: red">*</span> : </label>
                <input type="text" class="form-control" placeholder="Masukkan nama pengguna" style="width: 90%;" v-model="form.name" required>
              </div>
          </li>
          <li>
              <div class="form-group mb-0" style="margin-top: -20px;">
                <label>Email<span style="color: red">*</span> : </label>
                <input type="email" class="form-control" placeholder="Masukkan email yang valid" style="width: 90%;" v-model="form.email" required>
              </div>
          </li>
          <li>
              <div class="form-group">
                <label>Password<span style="color: red">*</span> : </label>
                <input type="password" class="form-control" placeholder="Masukkan password" style="width: 90%;" v-model="form.password" required>
              </div>
          </li>
          <li>
              <div class="form-group" style="margin-top: -20px;">
                <label>Confirmation Password<span style="color: red">*</span> : </label>
                <input type="password" class="form-control" placeholder="Masukkan ulang password" style="width: 90%;" v-model="password_confirmation" required>
              </div>
          </li>
          <li>
              <div class="form-group" style="margin-top: -20px;">
                <label>Nama Aplikasi<span style="color: red">*</span> : </label>
                <input type="text" class="form-control" style="width: 90%;" placeholder="ex: Lenna - Virtual Assistant" v-model="form.nama_aplikasi">
              </div>
          </li>
          <li>
              <div class="form-group" style="margin-top: -20px;">
                <label for="judul">Your package Apps (Google Play) : </label>
                <input type="text" class="form-control" name="judul" style="width: 90%;" placeholder="ex: ai.lenna.assistant" v-model="form.app_google_play">
              Bagaimana cara mendapatkan package tersebut ? <a href="#" v-b-modal.modal-1>Klik disini</a>
              </div>
              <b-modal id="modal-1" title="Tata Cara Mendapatkan id Package Google Play">
                <p class="my-4">
                  1. Bisa dengan melakukan search pada google search engine nama aplikasi anda.<br>
                  2. Kemudian pilih yang melakukan link ke <strong>google play</strong>.<br>
                  <img src="@/assets/img/helps/googleplay1.jpg" class="w-100" alt="Google Play Help 1">
                  3. Di url atas terdapat <strong>id package name</strong> seperti pada gambar berikut, kemudian anda salin ke dalam input form ini.<br>
                  <img src="@/assets/img/helps/googleplay2.jpg" class="w-100" alt="Google Play Help 2">
                </p>
              </b-modal>
          </li>
          <li>
              <div class="form-group" style="margin-top: -20px;">
                <label for="judul">Your id Apps (Apps Store) : </label>
                <input type="text" class="form-control" name="judul" placeholder="ex: 1460548724" style="width: 90%;" v-model="form.app_apps_store">
                Bagaimana cara mendapatkan id tersebut ? <a href="#" v-b-modal.modal-2>Klik disini</a>
              </div>
              <b-modal id="modal-2" title="Tata Cara Mendapatkan id Package Google Play">
                <p class="my-4">
                  1. Bisa dengan melakukan search pada google search engine nama aplikasi anda.<br>
                  2. Kemudian pilih yang melakukan link ke <strong>apps store</strong>.<br>
                  <img src="@/assets/img/helps/appstore1.jpg" class="w-100" alt="App Store Help 1">
                  3. Di url atas terdapat <strong>id</strong> yang hanya berupa <strong>angka</strong> seperti pada gambar berikut, kemudian anda salin ke dalam input form ini.<br>
                  <img src="@/assets/img/helps/appstore2.jpg" class="w-100" alt="App Store Help 2">
                </p>
              </b-modal>
          </li>
          <li>
              <div class="form-group" style="margin-top: -20px;">
                <label for="judul">Keyword for Instagram<span style="color: red">*</span> : </label>
                <div class="input-group" style="width: 90%;">
                  <div class="input-group-prepend">
                    <div class="input-group-text">
                      <i class="fas fa-hashtag"></i>
                    </div>
                  </div>
                  <input type="text" class="form-control" name="judul" placeholder="ex: lennaassistant" v-model="form.keyword_ig">
                </div>
              </div>
          </li>
          <li>
              <div class="form-group" style="margin-top: -20px;">
                <label for="judul">Keyword for Twitter<span style="color: red">*</span> : </label>
                <div class="input-group" style="width: 90%;">
                  <div class="input-group-prepend">
                    <div class="input-group-text">
                      <i class="fas fa-hashtag"></i>
                    </div>
                  </div>
                  <input type="text" class="form-control" name="judul" placeholder="ex: lennaassistant" style="width: 90%;" v-model="form.keyword_twitter">
                </div>
              </div>
          </li>
          <li>
              <div class="form-group">
                <label for="judul">Kenapa menggunaan Lenna Analytic ? </label>
                <textarea class="form-control" name="judul" style="width: 90%;" placeholder="ex: ai.lenna.assistant" v-model="form.description"></textarea>
              </div>
          </li>
          <li>
              <div class="form-group" style="margin-top: -20px;">
                <span style="color: red">*</span> is required.
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
          <button v-on:click="submitForm" class="btn-blue" style="margin: -3px 30px; padding: 10px;">Registrasi</button>
        </slot>
      </footer>
  </div>
</modal>
</template>
<script>
import { mapActions } from 'vuex'
import store from '@/store'
// Import component
import Loading from 'vue-loading-overlay';
// Import stylesheet
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
            password: '',
            nama_aplikasi: '',
            app_google_play: '',
            app_apps_store: '',
            keyword_ig: '',
            keyword_twitter: '',
            description: '',
            is_active: 0
        },
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
  methods:{
      ...mapActions({
        register: 'auth/register'
      }),
      async submitForm(e){
          this.isLoading = true
          if(this.isAgree){
            if(this.form.name && this.form.email && this.form.password && this.password_confirmation && this.form.keyword_ig && this.form.keyword_twitter && this.form.description && this.form.nama_aplikasi){
              if(this.password_confirmation === this.form.password){
                this.register(this.form).then(() => {
                  console.log(store.state.auth.successRegis)
                  if(store.state.auth.successRegis.status == 200){
                    this.isLoading = false
                    this.$toast.success(store.state.auth.successRegis.data.message, 'Success', this.notificationSystem.options.success)
                    setTimeout( () => this.$router.go(), 5000)
                  }else{
                    this.isLoading = false
                    this.$toast.warning(store.state.auth.successRegis.data.message, 'Failed', this.notificationSystem.options.warning)
                  }
                })
              }else{
                this.isLoading = false
                this.$toast.warning('Your password does not match!', 'Failed', this.notificationSystem.options.warning)
              }
            }
            this.errors = [];
            if(!this.form.name) this.errors.push("Name");
            if(!this.form.email) this.errors.push("Email");
            if(!this.form.password) this.errors.push("Password");
            if(!this.password_confirmation) this.errors.push("Confirmation Password");
            if(!this.form.keyword_ig) this.errors.push("Your Keyword for Instagram");
            if(!this.form.keyword_twitter) this.errors.push("Your Keyword for Twitter");
            if(!this.form.description) this.errors.push("Description");
            if(!this.form.nama_aplikasi) this.errors.push("Nama Aplikasi");
            e.preventDefault();
          }else{
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