import axios from 'axios'
export default ({
    namespaced: true,
    state: {
        apiconfig: [],
        api: [],
        param: {
            access_token: null,
            id: null
        },
        param_api: []
    },
    mutations: {
        SET_API(state, apiconfig) {
            state.apiconfig = apiconfig
        },
        SET_UBAH(state, api) {
            state.api = api
        },
    },
    actions: {
        async updateApi(context) {
            let response = await axios.put('http://127.0.0.1:5000/apiconfig/' + this.state.api.id, this.state.auth.param_api, {
                headers: {
                    Authorization: 'Bearer ' + this.state.api.param.access_token //the token is a variable which holds the token
                }
            });
            return context.commit("SET_UBAH", response);
        },
        async getApi(context) {
            let response = await axios.get('http://127.0.0.1:5000/apiconfig', {
                headers: {
                    Authorization: 'Bearer ' + this.state.post.param.access_token //the token is a variable which holds the token
                }
            });
            context.commit("SET_API", response.data.values);
        },
    },

    modules: {

    }
})
