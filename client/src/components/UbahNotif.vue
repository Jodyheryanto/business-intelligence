<template>
  <modal 
    name="modal-ubah-notif"
    transition="nice-modal-fade"
    height="500" 
    :scrollable="true"
    :delay="100"
    :adaptive="true">
  <loading :active.sync="isLoading" 
      :is-full-page="fullPage"></loading>
  <div class="example-modal-content">
      <h3 style="margin: 15px 20px;">Form Ubah Notification</h3>
      <hr>
      <p v-if="errors.length" style="margin-left: 25px;">
          <b>Please correct the following error(s):</b>
          <b v-for="(error,index) in errors" v-bind:key="index" style="color: red;"> {{ error }},</b><b style="color: red;"> Required</b>
      </p>
      <br>
      <ul type="none">
          <li>
              <div class="form-group" style="margin-top: -20px;">
                <label for="judul">Judul : </label>
                <input type="text" class="form-control" name="judul" style="width: 90%;" v-model="form.title" required>
              </div>
          </li>
          <li>
              <div class="form-group mb-0" style="margin-top: -20px; width: 90%;">
                <label for="deskripsi">Deskripsi : </label>
                <ckeditor :editor="editor" v-model="form.description" :config="editorConfig"></ckeditor>
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
            title: '',
            description: '',
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
        }
      }
  },
  mounted() {
    this.$eventBus.$on("datafromtableNotif", (x) => {
      this.neww = x;
      this.form.title = this.neww.title
      this.form.description = this.neww.description
      store.state.notification.param.id = this.neww.id
    });
  },
  methods:{
      ...mapActions({
        changeNotif: 'notification/changeNotif'
      }),
      async submitForm(){
          this.isLoading = true
          if(this.form.title && this.form.description){
            store.state.notification.param_notif = this.form
            store.state.notification.param.access_token = this.$cookie.get('user_token')
            this.changeNotif().then(() => {
              if(store.state.notification.notif.status == 200){
                this.isLoading = false
                this.$toast.success(store.state.notification.notif.data.message, 'Success', this.notificationSystem.options.success)
                setTimeout( () => location.reload(), 3000)
              }else{
                this.isLoading = false
                this.$toast.warning(store.state.notification.notif.data.message, 'Failed', this.notificationSystem.options.warning)
              }
            })
          }
          this.errors = [];
          if(!this.form.title) this.errors.push("Judul");
          if(!this.form.description) this.errors.push("Deskripsi");
      }
  }
}
</script>

<style scope>
.v--modal-box {
  margin: 10px;
}
</style>