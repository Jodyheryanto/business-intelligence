import axios from 'axios'
export default ({
    namespaced: true,
    state: {
        success: false,
        successRegis: false,
        successUbah: false,
        ubahPass: [],
        successDelete: false,
        message: '',
        name: '',
        access_token: '',
        roleTemp: null,
        role: null,
        googleplay: '',
        appstore: '',
        instagram: '',
        twitter: '',
        user_id: null,
        data_user: [],
        param_user: [],
        param_password: [],
        nama_aplikasi: '',
        is_active: null,
        user: []
        // token: null,
        // user: null
    },
    getters: {
        authenticated(state) {
            return state.success
        },
        user(state) {
            return state.name
        }
        // user(state) {
        //     return state.user
        // }
    },
    mutations: {
        SET_SUCCESS(state, success) {
            state.success = success
        },
        SET_ACTIVE(state, is_active) {
            state.is_active = is_active
        },
        SET_SUCCESS_REGIS(state, success) {
            state.successRegis = success
        },
        SET_MESSAGE(state, message) {
            state.message = message
        },
        SET_NAME(state, name) {
            state.name = name
        },
        SET_ROLE(state, role) {
            state.role = role
        },
        SET_APLIKASIGP(state, googleplay) {
            state.googleplay = googleplay
        },
        SET_APLIKASIAS(state, appstore) {
            state.appstore = appstore
        },
        SET_INSTAGRAM(state, keyword_ig) {
            state.instagram = keyword_ig
        },
        SET_TWITTER(state, keyword_twitter) {
            state.twitter = keyword_twitter
        },
        SET_NAMA_APLIKASI(state, nama_aplikasi) {
            state.nama_aplikasi = nama_aplikasi
        },
        SET_USERS(state, data_user) {
            state.data_user = data_user
        },
        SET_UBAH(state, ubah) {
            state.successUbah = ubah
        },
        SET_UBAHPASS(state, ubahPass) {
            state.UbahPass = ubahPass
        },
        SET_DELETE(state, Delete) {
            state.successDelete = Delete
        },
        SET_TOKEN(state, token_access) {
            state.access_token = token_access
        },
        SET_USER(state, user) {
            state.user = user
        }
        // SET_TOKEN(state, token) {
        //     state.token = token
        // },
        // SET_USER(state, data) {
        //     state.user = data
        // }
    },
    actions: {
        async register({ dispatch }, credentials) {
            await axios.post('http://127.0.0.1:5000/users', credentials).then(response => {
                return dispatch('attemptRegister', response)
            }).catch((error) => {
                return dispatch('attemptRegister', error.response)
            })
        },
        async ubah(context) {
            let response = await axios.put('http://127.0.0.1:5000/users/' + this.state.auth.user_id, this.state.auth.param_user, {
                headers: {
                    Authorization: 'Bearer ' + this.state.post.param.access_token //the token is a variable which holds the token
                }
            });
            if (response.data.message === 'Successfully update data!')
                return context.commit("SET_UBAH", true);
            else {
                return context.commit("SET_UBAH", false);
            }
        },
        async ubahPassword(context) {
            let response = await axios.put('http://127.0.0.1:5000/users/password/' + this.state.auth.user_id, this.state.auth.param_password, {
                headers: {
                    Authorization: 'Bearer ' + this.state.post.param.access_token //the token is a variable which holds the token
                }
            });
            context.commit("SET_UBAHPASS", response);
        },
        async ubahStatus(context) {
            let response = await axios.put('http://127.0.0.1:5000/users/ubahstatus/' + this.state.auth.user_id, this.state.auth.is_active, {
                headers: {
                    Authorization: 'Bearer ' + this.state.post.param.access_token //the token is a variable which holds the token
                }
            });
            if (response.data.message === 'Successfully update data!')
                return context.commit("SET_UBAH", true);
            else {
                return context.commit("SET_UBAH", false);
            }
        },
        async delete(context) {
            let response = await axios.delete('http://127.0.0.1:5000/users/' + this.state.auth.user_id)
            if (response.data.message === 'Successfully delete data!')
                return context.commit("SET_DELETE", true);
            else {
                return context.commit("SET_DELETE", false);
            }
        },
        async getUsers(context) {
            let response = await axios.get('http://127.0.0.1:5000/users', {
                headers: {
                    Authorization: 'Bearer ' + this.state.post.param.access_token //the token is a variable which holds the token
                }
            });
            context.commit("SET_USERS", response.data.values);
        },
        async signIn({ dispatch }, credentials) {
            // if (credentials.email === "admin" && credentials.password === "admin") {
            //     this.state.roleTemp = 0
            //     let response = []
            //     response.success = true
            //     return dispatch('attempt', response)
            // } else {
            // let response = 
            await axios.post('http://127.0.0.1:5000/login', credentials).then(response => {
                return dispatch('attempt', response)
            }).catch((error) => {
                return dispatch('attempt', error.response)
            })
            // this.state.roleTemp = 1
            // }
        },
        async attempt({ commit }, response) {
            if (response.status === 200) {
                response = response.data.values
                commit('SET_USER', response)
            } else {
                commit('SET_USER', {data: { success: false, message: response.data.message }})
            }
        },
        attemptRegister({ commit }, response) {
            commit('SET_SUCCESS_REGIS', response)
        },
        signOut({ commit }) {
            commit('SET_SUCCESS', false)
            commit('SET_ROLE', null)
            commit('SET_NAME', null)
            commit('SET_INSTAGRAM', null)
            commit('SET_APLIKASIGP', null)
            commit('SET_APLIKASIAS', null)
            commit('SET_TWITTER', null)
        }
    },

    modules: {

    }
})
