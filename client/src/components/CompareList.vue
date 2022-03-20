<template>
    <div class="row">
        <div class="col-12 col-lg-4">
            <div class="card">
                <div class="card-header">
                    <h4>Posts Total</h4>
                </div>
                <div class="card-body">
                    <div style="text-align: right; margin-top: 20px"><h4><i v-if="counts.post2-counts.post1 > 0" class="fas fa-arrow-up" style="color: green;"></i><i v-else-if="counts.post2-counts.post1 === 0" style="color: gray;">-</i><i v-else class="fas fa-arrow-down" style="color: red;"></i> {{ counts.post2 - counts.post1 }} ({{ counts.post1 }})</h4></div>
                    <div style="text-align: center;  margin-top: -30px;"><h1 style="font-size: 100px">{{ counts.post2 }}</h1><h4>Post</h4></div>
                </div>
            </div>
        </div>
        <div class="col-12 col-lg-4">
            <div class="card">
                <div class="card-header">
                    <h4>Negative Total</h4>
                </div>
                <div class="card-body">
                    <div style="text-align: right; margin-top: 20px"><h4><i v-if="counts.neg2-counts.neg1 > 0" class="fas fa-arrow-up" style="color: red;"></i><i v-else-if="counts.neg2-counts.neg1 === 0" style="color: gray;">-</i><i v-else class="fas fa-arrow-down" style="color: green;"></i> {{ counts.neg2 - counts.neg1 }} ({{ counts.neg1 }})</h4></div>
                    <div style="text-align: center;  margin-top: -30px;"><h1 style="font-size: 100px">{{ counts.neg2 }}</h1><h4>Post</h4></div>
                </div>
            </div>
        </div>
        <div class="col-12 col-lg-4">
            <div class="card">
                <div class="card-header">
                    <h4>Positive Total</h4>
                </div>
                <div class="card-body">
                    <div style="text-align: right; margin-top: 20px"><h4><i v-if="counts.pos2-counts.pos1 > 0" class="fas fa-arrow-up" style="color: green;"></i><i v-else-if="counts.pos2-counts.pos1 === 0" style="color: gray;">-</i><i v-else class="fas fa-arrow-down" style="color: red;"></i> {{ counts.pos2 - counts.pos1 }} ({{ counts.pos1 }})</h4></div>
                    <div style="text-align: center;  margin-top: -30px;"><h1 style="font-size: 100px">{{ counts.pos2 }}</h1><h4>Post</h4></div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import store from '@/store'
export default {
    data(){
        return{
            counts: {
                post1: 0,
                post2: 0,
                neg1: 0,
                neg2: 0,
                pos1: 0,
                pos2: 0,
                aplikasi: ''
            }, 
        }
    },
    async mounted() {
        this.fillData()
        this.fillData2()
    },
    methods: {
        fillData(){
            let data = store.state.post.DataCompare1
            var post1_temp = 0
            var pos1_temp = 0
            var neg1_temp = 0
            for(var i=0; i < data.length; i++){
                post1_temp += 1
                if(data[i].sentiment === 0){
                    neg1_temp += 1
                }else{
                    pos1_temp += 1
                }
            }
            this.counts.post1 = post1_temp
            this.counts.pos1 = pos1_temp
            this.counts.neg1 = neg1_temp
        },
        fillData2(){
            let data = store.state.post.DataCompare2
            var post2_temp = 0
            var pos2_temp = 0
            // var neu2_temp = 0
            var neg2_temp = 0
            for(var i=0; i < data.length; i++){
                post2_temp += 1
                if(data[i].sentiment === 0){
                    neg2_temp += 1
                }else{
                    pos2_temp += 1
                }
            }
            this.counts.post2 = post2_temp
            this.counts.pos2 = pos2_temp
            this.counts.neg2 = neg2_temp
        }
    },
}
</script>