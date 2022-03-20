import axios from 'axios'
export default ({
    namespaced: true,
    state: {
        DataNotif: [],
        param: {
            user_id: null,
            access_token: [],
            preview: false,
            id: null
        },
        param_notif: [],
        notif: []
    },
    getters: {},
    mutations: {
        SET_NOTIF(state, notif) {
            state.DataNotif = notif
        },
        SET_CNOTIF(state, notif) {
            state.notif = notif
        }
    },
    actions: {
        async loadDataNotif(context) {
            if (this.state.notification.param.user_id == 1 && this.state.notification.param.preview == false) {
                var result = await axios.get("http://127.0.0.1:5000/notifications", {
                    headers: {
                        Authorization: 'Bearer ' + this.state.notification.param.access_token //the token is a variable which holds the token
                    }
                });
            } else {
                result = await axios.get("http://127.0.0.1:5000/notifications?" + "user_id=" + this.state.notification.param.user_id, {
                    headers: {
                        Authorization: 'Bearer ' + this.state.notification.param.access_token //the token is a variable which holds the token
                    }
                });
            }
            context.commit("SET_NOTIF", result.data.values);
        },
        async ubahStatusNotif() {
            return await axios.get("http://127.0.0.1:5000/notifications/" + this.state.notification.param.id, {
                headers: {
                    Authorization: 'Bearer ' + this.state.notification.param.access_token //the token is a variable which holds the token
                }
            });
        },
        async createNotif(context) {
            let response = await axios.post("http://127.0.0.1:5000/notifications", this.state.notification.param_notif, {
                headers: {
                    Authorization: 'Bearer ' + this.state.notification.param.access_token //the token is a variable which holds the token
                }
            });
            context.commit("SET_CNOTIF", response);
        },
        async changeNotif(context) {
            let response = await axios.put("http://127.0.0.1:5000/notifications/" + this.state.notification.param.id, this.state.notification.param_notif, {
                headers: {
                    Authorization: 'Bearer ' + this.state.notification.param.access_token //the token is a variable which holds the token
                }
            });
            context.commit("SET_CNOTIF", response);
        },
        async delete(context) {
            let response = await axios.delete("http://127.0.0.1:5000/notifications/" + this.state.notification.param.id, {
                headers: {
                    Authorization: 'Bearer ' + this.state.notification.param.access_token //the token is a variable which holds the token
                }
            });
            context.commit("SET_CNOTIF", response);
        }
    }
})
