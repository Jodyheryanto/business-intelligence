<template>
  <modal 
    name="modal-tambah-help"
    transition="nice-modal-fade"
    height="500" 
    :scrollable="true"
    :delay="100"
    :adaptive="true">
  <loading :active.sync="isLoading" 
      :is-full-page="fullPage"></loading>
  <div class="example-modal-content">
      <h3 style="margin: 15px 20px;">Form Tambah Help</h3>
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
          <button v-on:click="submitForm" class="btn-blue" style="margin: -3px 30px; padding: 10px;">Tambah Data</button>
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
      Loading,
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
  methods:{
      ...mapActions({
        createHelp: 'help/createHelp'
      }),
      async submitForm(){
          this.isLoading = true
          if(this.form.title && this.form.description){
            store.state.help.param_help = this.form
            store.state.help.param_help.access_token = this.$cookie.get('user_token')
            this.createHelp().then(() => {
              if(store.state.help.help.status == 200){
                this.isLoading = false
                this.$toast.success(store.state.help.help.data.message, 'Success', this.notificationSystem.options.success)
                setTimeout( () => location.reload(), 3000)
              }else{
                this.isLoading = false
                this.$toast.warning(store.state.help.help.data.message, 'Failed', this.notificationSystem.options.warning)
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
.ck-content {   
  min-height: 150px; 
}
</style>