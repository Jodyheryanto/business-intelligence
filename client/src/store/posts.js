import axios from 'axios'
export default ({
    namespaced: true,
    state: {
        DataPost: [],
        DataCompare1: [],
        DataCompare2: [],
        DataPostFilter: [],
        countGooglePlay: 0,
        CompareDate: {
            start1: null,
            start2: null,
            end1: null,
            end2: null
        },
        filter: {
            sources: [],
            success: false
        },
        param: {
            startDate: null,
            endDate: null,
            user_id: null,
            // googleplay: null,
            // appstore: null,
            // twitter: null,
            // instagram: null,
            // nama_aplikasi: null,
            sentiments: [],
            access_token: []
        }
    },
    getters: {},
    mutations: {
        SET_POST(state, post) {
            state.DataPost = post
        },
        SET_COUNT(state, count) {
            state.countGooglePlay = count
        }
    },
    actions: {
        async loadDataPost(context) {
            let post_temp = []
            // var result = await axios.get("http://127.0.0.1:5000/api/posts");
            // if (this.state.post.param.sentiments.length === 3 && this.state.post.param.aplikasi !== "") {
            //     var result = await axios.get("http://127.0.0.1:5000/getpost?tanggal_awal=" + this.state.post.param.startDate + "&tanggal_akhir=" + this.state.post.param.endDate + "&aplikasi=" + this.state.post.param.aplikasi + "&sentiment=" + this.state.post.param.sentiments[0] + "," + this.state.post.param.sentiments[1] + "," + this.state.post.param.sentiments[2]);
            // } else 
            if (this.state.post.param.sentiments.length === 2) {
                let param_aplikasi = ["googleplay", "appstore", "instagram", "twitter"]
                //     {
                //     sumber: "googleplay",
                //     nama_param: "aplikasi",
                //     nama_aplikasi: this.state.post.param.nama_aplikasi,
                //     keyword: this.state.post.param.googleplay
                // },
                // {
                //     sumber: "instagram",
                //     nama_param: "keyword",
                //     nama_aplikasi: this.state.post.param.nama_aplikasi,
                //     keyword: this.state.post.param.instagram
                // },
                // {
                //     sumber: "twitter",
                //     nama_param: "keyword",
                //     nama_aplikasi: this.state.post.param.nama_aplikasi,
                //     keyword: this.state.post.param.twitter
                // }]
                for (var i = 0; i < param_aplikasi.length; i++){
                    var result = await axios.get("http://127.0.0.1:5000/get" + param_aplikasi[i] + "?tanggal_awal=" + this.state.post.param.startDate + "&tanggal_akhir=" + this.state.post.param.endDate + "&user_id=" + this.state.post.param.user_id + "&sentiment=" + this.state.post.param.sentiments[0] + "," + this.state.post.param.sentiments[1], {
                        headers: {
                            Authorization: 'Bearer ' + this.state.post.param.access_token //the token is a variable which holds the token
                        }
                    });
                    for (var j = 0; j < result.data.values.length; j++) {
                        post_temp.push({
                            aplikasi: result.data.values[j].aplikasi,
                            id: result.data.values[j].id,
                            link_review: result.data.values[j].link_review,
                            post: result.data.values[j].post,
                            rating: result.data.values[j].rating,
                            sentiment: result.data.values[j].sentiment,
                            sumber: result.data.values[j].sumber,
                            tanggal_post: result.data.values[j].tanggal_post,
                            user_avatar: result.data.values[j].user_avatar,
                            user_name: result.data.values[j].user_name
                        })
                    }
                }
            } else if (this.state.post.param.sentiments.length === 1) {
                let param_aplikasi = ["googleplay", "appstore", "instagram", "twitter"]
                for (i = 0; i < param_aplikasi.length; i++) {
                    result = await axios.get("http://127.0.0.1:5000/get" + param_aplikasi[i] + "?tanggal_awal=" + this.state.post.param.startDate + "&tanggal_akhir=" + this.state.post.param.endDate + "&user_id=" + this.state.post.param.user_id + "&sentiment=" + this.state.post.param.sentiments[0], {
                        headers: {
                            Authorization: 'Bearer ' + this.state.post.param.access_token //the token is a variable which holds the token
                        }
                    });
                    for (j = 0; j < result.data.values.length; j++) {
                        post_temp.push({
                            aplikasi: result.data.values[j].aplikasi,
                            id: result.data.values[j].id,
                            link_review: result.data.values[j].link_review,
                            post: result.data.values[j].post,
                            rating: result.data.values[j].rating,
                            sentiment: result.data.values[j].sentiment,
                            sumber: result.data.values[j].sumber,
                            tanggal_post: result.data.values[j].tanggal_post,
                            user_avatar: result.data.values[j].user_avatar,
                            user_name: result.data.values[j].user_name
                        })
                    }
                }
            }// else if (this.state.post.param.sentiments.length === 3) {
            //     result = await axios.get("http://127.0.0.1:5000/getpost?tanggal_awal=" + this.state.post.param.startDate + "&tanggal_akhir=" + this.state.post.param.endDate + "&sentiment=" + this.state.post.param.sentiments[0] + "," + this.state.post.param.sentiments[1] + "," + this.state.post.param.sentiments[2]);
            // } 
            else if (this.state.post.param.sentiments.length === 2 && this.state.post.param.user_id === 1) {
                let param_sumber = ['googleplay', 'instagram', 'appstore', 'twitter']
                for (i = 0; i < param_sumber.length; i++) {
                    result = await axios.get("http://127.0.0.1:5000/get" + param_sumber[i] + "?tanggal_awal=" + this.state.post.param.startDate + "&tanggal_akhir=" + this.state.post.param.endDate + "&sentiment=" + this.state.post.param.sentiments[0] + "," + this.state.post.param.sentiments[1], {
                        headers: {
                            Authorization: 'Bearer ' + this.state.post.param.access_token //the token is a variable which holds the token
                        }
                    });
                    for (j = 0; j < result.data.values.length; j++) {
                        post_temp.push({
                            aplikasi: result.data.values[j].aplikasi,
                            id: result.data.values[j].id,
                            link_review: result.data.values[j].link_review,
                            post: result.data.values[j].post,
                            rating: result.data.values[j].rating,
                            sentiment: result.data.values[j].sentiment,
                            sumber: result.data.values[j].sumber,
                            tanggal_post: result.data.values[j].tanggal_post,
                            user_avatar: result.data.values[j].user_avatar,
                            user_name: result.data.values[j].user_name
                        })
                    }
                }
            } else if (this.state.post.param.sentiments.length === 1 && this.state.post.param.user_id === 1) {
                let param_sumber = ['googleplay', 'instagram', 'appstore', 'twitter']
                for (i = 0; i < param_sumber.length; i++) {
                    result = await axios.get("http://127.0.0.1:5000/get" + param_sumber[i] + "?tanggal_awal=" + this.state.post.param.startDate + "&tanggal_akhir=" + this.state.post.param.endDate + "&sentiment=" + this.state.post.param.sentiments[0], {
                        headers: {
                            Authorization: 'Bearer ' + this.state.post.param.access_token //the token is a variable which holds the token
                        }
                    });
                    for (j = 0; j < result.data.values.length; j++) {
                        post_temp.push({
                            aplikasi: result.data.values[j].aplikasi,
                            id: result.data.values[j].id,
                            link_review: result.data.values[j].link_review,
                            post: result.data.values[j].post,
                            rating: result.data.values[j].rating,
                            sentiment: result.data.values[j].sentiment,
                            sumber: result.data.values[j].sumber,
                            tanggal_post: result.data.values[j].tanggal_post,
                            user_avatar: result.data.values[j].user_avatar,
                            user_name: result.data.values[j].user_name
                        })
                    }
                }
            }
            //var result = await axios.get("https://idreambooks.com/api/books/reviews.json?isbn=9781101475973&key=27d6ec438a683c67ddf256d4706aa3bf31053d91");
            context.commit("SET_POST", post_temp);
        },
        async loadCountPost(context) {
            var result = await axios.get("http://127.0.0.1:5000/api/posts");
            var countGP = 0
            for (var i = 0; i < result.data.data.length; i++) {
                if (result.data.data[i].sumber === 'Google Play') {
                    countGP += 1
                }
            }
            context.commit("SET_COUNT", countGP);
        },
    }
})
