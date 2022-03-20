import axios from 'axios'
export default ({
    namespaced: true,
    state: {
        DataHelp: [],
        param: {
            access_token: [],
            id: null
        },
        help: [],
        param_help: []
    },
    getters: {},
    mutations: {
        SET_HELP(state, help) {
            state.DataHelp = help
        },
        SET_CHELP(state, help) {
            state.help = help
        }
    },
    actions: {
        async loadDataHelp(context) {
            var result = await axios.get("http://127.0.0.1:5000/helps", {
                headers: {
                    Authorization: 'Bearer ' + this.state.help.param.access_token //the token is a variable which holds the token
                }
            });
            context.commit("SET_HELP", result.data.values);
        },
        async createHelp(context) {
            let response = await axios.post("http://127.0.0.1:5000/helps", this.state.help.param_help, {
                headers: {
                    Authorization: 'Bearer ' + this.state.help.param.access_token //the token is a variable which holds the token
                }
            });
            context.commit("SET_CHELP", response);
        },
        async changeHelp(context) {
            let response = await axios.put("http://127.0.0.1:5000/helps/" + this.state.help.param.id, this.state.help.param_help, {
                headers: {
                    Authorization: 'Bearer ' + this.state.help.param.access_token //the token is a variable which holds the token
                }
            });
            context.commit("SET_CHELP", response);
        },
        async delete(context) {
            let response = await axios.delete("http://127.0.0.1:5000/helps/" + this.state.help.param.id, {
                headers: {
                    Authorization: 'Bearer ' + this.state.help.param.access_token //the token is a variable which holds the token
                }
            });
            context.commit("SET_CHELP", response);
        }
    }
})
