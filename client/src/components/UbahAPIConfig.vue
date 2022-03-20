<template>
  <modal 
    name="modal-ubah-api"
    transition="nice-modal-fade"
    height="auto" 
    :scrollable="true"
    :delay="100"
    :adaptive="true">
  <loading :active.sync="isLoading" 
      :is-full-page="fullPage"></loading>
  <div class="example-modal-content">
      <h3 style="margin: 15px 20px;">Form Ubah API</h3>
      <hr>
      <p v-if="errors.length" style="margin-left: 25px;">
          <b>Please correct the following error(s):</b>
          <b v-for="(error,index) in errors" v-bind:key="index" style="color: red;"> {{ error }},</b><b style="color: red;"> Required</b>
      </p>
      <br>
      <ul type="none">
          <li>
              <div class="form-group" style="margin-top: -20px;">
                <label>URL API : </label>
                <input type="text" class="form-control" style="width: 90%;" v-model="form.url_api" required>
              </div>
          </li>
          <li>
              <div class="form-group" style="margin-top: -20px;">
                <label for="deskripsi">Parameter 1 : </label>
                <input type="text" class="form-control" style="width: 90%;" v-model="form.param1" required>
              </div>
          </li>
          <li>
              <div class="form-group" style="margin-top: -20px;">
                <label>Parameter 2 : </label>
                <input type="text" class="form-control" name="judul" style="width: 90%;" v-model="form.param2" required>
              </div>
          </li>
          <li>
              <div class="form-group" style="margin-top: -20px;">
                <label>Consumer Key : </label>
                <input type="text" class="form-control" style="width: 90%;" v-model="form.consumer_key" required>
              </div>
          </li>
          <li>
              <div class="form-group" style="margin-top: -20px;">
                <label>Consumer Secret : </label>
                <input type="text" class="form-control" style="width: 90%;" v-model="form.consumer_secret" required>
              </div>
          </li>
          <li>
              <div class="form-group" style="margin-top: -20px;">
                <label >Access Token : </label>
                <input type="text" class="form-control" style="width: 90%;" v-model="form.access_token" required>
              </div>
          </li>
          <li>
              <div class="form-group" style="margin-top: -20px;">
                <label>Access Token Secret : </label>
                <input type="text" class="form-control" style="width: 90%;" v-model="form.access_token_secret" required>
              </div>
          </li>
      </ul>
      <footer class="modal-footer">
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
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";
export default {
  components: {
      Loading
  },
  data() {
      return {
        isLoading: false,
        fullPage: true,
        CKValue: "",
        editor: ClassicEditor,
        editorConfig: {},
        form: {
            url_api: '',
            param1: '',
            param2: '',
            consumer_key: '',
            consumer_secret: '',
            access_token: '',
            access_token_secret: '',
        },
        errors: [],
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
        neww: []
      }
  },
  mounted() {
    this.$eventBus.$on("datafromtableAPI", (x) => {
      this.neww = x;
      this.form.url_api = this.neww.url_api
      this.form.param1 = this.neww.param1
      this.form.param2 = this.neww.param2
      this.form.consumer_key = this.neww.consumer_key
      this.form.consumer_secret = this.neww.consumer_secret
      this.form.access_token = this.neww.access_token
      this.form.access_token_secret = this.neww.access_token_secret
      store.state.api.param.id = this.neww.id
    });
  },
  methods:{
      ...mapActions({
        changeNotif: 'api/changeAPI'
      }),
      async submitForm(){
          this.isLoading = true
          if(this.form.url_api && this.form.param1 && this.form.param2 && this.form.consumer_key && this.form.consumer_secret && this.form.access_token && this.form.consumer_secret){
            store.state.api.param_api = this.form
            store.state.api.param.access_token = this.$cookie.get('user_token')
            this.changeNotif().then(() => {
              if(store.state.api.api.status == 200){
                this.isLoading = false
                this.$toast.success(store.state.api.api.data.message, 'Success', this.notificationSystem.options.success)
                setTimeout( () => location.reload(), 3000)
              }else{
                this.isLoading = false
                this.$toast.warning(store.state.api.api.data.message, 'Failed', this.notificationSystem.options.warning)
              }
            })
          }
          this.errors = [];
          if(!this.form.url_api) this.errors.push("URL API");
          if(!this.form.param1) this.errors.push("Parameter 1");
          if(!this.form.param2) this.errors.push("Parameter 2");
          if(!this.form.consumer_key) this.errors.push("Consumer Key");
          if(!this.form.consumer_secret) this.errors.push("Consumer Secret");
          if(!this.form.access_token) this.errors.push("Access Token");
          if(!this.form.access_token_secret) this.errors.push("Access Token Secret");
      }
  }
}
</script>

<style scope>
.v--modal-box {
  margin: 10px;
}
</style>