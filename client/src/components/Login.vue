<template>
    <div>
        <section class="section">
        <loading :active.sync="isLoading" 
            :is-full-page="fullPage"></loading>
        <div class="container mt-5">
        <div class="row">
        <div class="col-12 col-sm-8 offset-sm-2 col-md-6 offset-md-3 col-lg-6 offset-lg-3 col-xl-4 offset-xl-4">
        <div class="login-brand">
            <!-- <img src="../assets/logo_lenna_color.png" alt="logo" height="75px"> -->
            <h1>LOGO</h1>
        </div>

        <div class="card card-primary">
            <div class="card-header"><h4>Login</h4></div>

            <div class="card-body">
                <div class="needs-validation">
                    <div class="form-group">
                        <label for="email">Email</label>
                        <input type="email" class="form-control" v-model="form.email" tabindex="1" required autofocus v-on:keyup.enter="submit" placeholder="Masukkan email">
                    </div>

                    <div class="form-group">
                        <label for="password">Password</label>    
                        <div class="input-group">
                            <input :type="passwordFieldType" v-model="form.password" class="form-control" name="password" tabindex="2" required v-on:keyup.enter="submit" placeholder="Masukkan password">
                            <button class="buttonTransparent" type="password" @click="switchVisibility"><i class="fas fa-eye eyeClass"></i></button>
                        </div>
                    </div>

                    <div class="form-group">
                        <button v-on:click.enter="submit" type="submit" class="btn btn-primary btn-lg btn-block" tabindex="4">
                        Login
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <div class="mt-5 text-muted text-center">
            Don't have an account? <a href="#" @click="$modal.show('example-adaptive')">Create One</a>
        </div>
    </div>
        </div>
    </div>
    </section>
    </div>
</template>
<script>
//import axios from 'axios'
import { mapActions } from 'vuex'
import store from '@/store'
// Import component
import Loading from 'vue-loading-overlay';
// Import stylesheet
import 'vue-loading-overlay/dist/vue-loading.css';
export default {
        name: 'Login',
        components: {
            Loading
        },
        data() {
            return {
                isLoading: false,
                fullPage: true,
                form: {
                    email: "",
                    password: ""
                },
                passwordFieldType: 'password',
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
        methods: {
            ...mapActions({
                signIn: 'auth/signIn'
            }),
            submit() {
                this.isLoading = true
                this.signIn(this.form).then(() => {
                    if(store.state.auth.user.data.success){
                        this.$cookie.set('user_success', store.state.auth.user.data.success, { expires: '30m' });
                        this.$cookie.set('user_id', store.state.auth.user.data.id, { expires: '30m' });
                        this.$cookie.set('user_name', store.state.auth.user.data.name, { expires: '30m' });
                        this.$cookie.set('user_role', store.state.auth.user.data.is_active, { expires: '30m' });
                        this.$cookie.set('user_token', store.state.auth.user.token_access, { expires: '30m' });
                        this.isLoading = false
                        this.$toast.success('You Succeeded Login!', 'Congratulation', this.notificationSystem.options.success)
                        setTimeout( () => this.$router.replace({
                            name: 'Home'
                        }), 3000)
                    }else{
                        this.isLoading = false
                        this.$toast.warning(store.state.auth.user.data.message, 'Failed', this.notificationSystem.options.warning)
                    }                   
                })
            },
            switchVisibility() {
                this.passwordFieldType = this.passwordFieldType === 'password' ? 'text' : 'password'
            }
        },
        mounted() {
            this.$cookie.set('filterClick', false);
            this.$cookie.set('startDate', null);
            this.$cookie.set('endDate', null);
        },
    }
</script>
<style scoped>
    .buttonTransparent {
        background-color: Transparent;
        background-repeat:no-repeat;
        border: none;
        cursor:pointer;
        overflow: hidden;
        outline:none;
        margin: 0 10px;
    }
    .eyeClass{
        color: #003777;
    }
</style>
