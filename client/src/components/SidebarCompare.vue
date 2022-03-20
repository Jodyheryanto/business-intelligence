<template>
    <div class="main-sidebar">
        <aside class="is_stuck">
            <ul class="sidebar-menu">
                <button type="button" title="Close Sidebar" v-if="$mq === 'mobile' || $mq === 'tablet'" @click="toggleBodyClassMini(kondisiMini, 'sidebar-gone')" style="margin: -7px 5px" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true" class="btn btn-icon btn-danger" style="background-color: red"><i class="fas fa-times"></i></span>
                </button>
                <li class="menu-header"><i class="fas fa-calendar-week"></i> Date Compare</li>

                <li><vc-date-picker mode='range' :value="rangeTgl" v-model='rangeTgl'/></li>
                <li style="text-align: center">vs.</li>
                <li><vc-date-picker mode='range' :value="rangeTgl2" v-model='rangeTgl2'/></li>
                <!-- <li class="menu-header"><i class="fas fa-filter"></i> Data Filtering</li>
                <li>
                    <a class="nav-link"><i class="fas fa-smile"></i><span>Sentiments</span></a>
                </li>
                <li>
                    <div class="col-auto my-1">
                        <div class="custom-control custom-checkbox mr-sm-2" v-for="(label_sentiment,index) in label_sentiments" v-bind:key="index">
                            <input type="checkbox" class="custom-control-input" :id="label_sentiment" :value="label_sentiment" v-model="userIdsSentiment" checked>
                            <label class="custom-control-label" :for="label_sentiment">{{ label_sentiment }}</label>
                        </div>
                    </div>
                </li>
                <li>
                    <a class="nav-link"><i class="fas fa-hashtag"></i><span>Sources</span></a>
                </li>
                <li>
                    <div class="col-auto my-1">
                        <div class="custom-control custom-checkbox mr-sm-2">
                            <input type="checkbox" class="custom-control-input" id="allSource" @click="selectAllSource" v-model="allSelectedSource">
                            <label class="custom-control-label" for="allSource">Select All</label>
                        </div>
                    </div>
                    <hr>
                    <div class="col-auto my-1">
                        <div class="custom-control custom-checkbox mr-sm-2" v-for="(label_source,index) in label_sources" v-bind:key="index">
                            <input type="checkbox" class="custom-control-input" :id="label_source" @click="selectSource" :value="label_source" v-model="userIdsSource">
                            <label class="custom-control-label" :for="label_source">{{ label_source }}</label>
                        </div>
                    </div>
                </li> -->
                <!-- <li>
                    <a class="nav-link"><i class="fas fa-money-check-alt"></i><span>Objects & Groups</span></a>
                </li>
                <li>
                    <div class="col-auto my-1">
                        <div class="custom-control custom-checkbox mr-sm-2">
                            <input type="checkbox" class="custom-control-input" id="allObject" @click="selectAllObject" v-model="allSelectedObject">
                            <label class="custom-control-label" for="allObject">Select All</label>
                        </div>
                    </div>
                    <hr>
                    <div class="col-auto my-1">
                        <div class="custom-control custom-checkbox mr-sm-2" v-for="(label_object,index) in label_objects" v-bind:key="index">
                            <input type="checkbox" class="custom-control-input" :id="label_object" @click="selectObject" :value="label_object" v-model="userIdsObject">
                            <label class="custom-control-label" :for="label_object">{{ label_object }}</label>
                        </div>
                    </div>
                </li> -->
                <li>
                    <button @click="filterMenu" class="btn btn-primary" style="margin: 20px 50px;"><i class="fas fa-search"></i> Filter</button>
                </li>
            </ul>
        </aside>
    </div>
</template>
<script>
// import store from '@/store'
import moment from 'moment'
export default {
data: function(){
    return {
        booleanUbah: true,
        // label_sentiments: ['Positive', 'Neutral', 'Negative'],
        // label_sources: [],
        // label_objects: [],
        // allSelectedSource: false,
        // userIdsSource: [],
        // userIdsSentiment: ['Positive', 'Neutral', 'Negative'],
        // allSelectedObject: false,
        // userIdsObject: [],
        rangeTgl: {
            start: this.addDays(new Date(), -60),
            end: this.addDays(new Date(), -30)
        },
        rangeTgl2: {
            start: this.addDays(new Date(), -30),
            end: new Date()
        },
        kondisiMini: true,
        success: false
    }
},
async mounted(){
    this.isBusy = true;
    this.rangeTgl.start = new Date(moment(this.$cookie.get('compare_start1')).format('YYYY'), moment(this.$cookie.get('compare_start1')).format('MM') - 1,  moment(this.$cookie.get('compare_start1')).format('DD'))
    this.rangeTgl.end = new Date(moment(this.$cookie.get('compare_end1')).format('YYYY'), moment(this.$cookie.get('compare_end1')).format('MM') - 1,  moment(this.$cookie.get('compare_end1')).format('DD'))
    this.rangeTgl2.start = new Date(moment(this.$cookie.get('compare_start2')).format('YYYY'), moment(this.$cookie.get('compare_start2')).format('MM') - 1,  moment(this.$cookie.get('compare_start2')).format('DD'))
    this.rangeTgl2.end = new Date(moment(this.$cookie.get('compare_end2')).format('YYYY'), moment(this.$cookie.get('compare_end2')).format('MM') - 1,  moment(this.$cookie.get('compare_end2')).format('DD'))
    // try {
    //     await this.$store.dispatch('source/loadSource')
    //     await this.$store.dispatch('object/loadObject')
    //     this.fillDataSource()
    //     this.fillDataObject()
    // } catch (ex) {
    //     this.error = "Failed to load data";
    // } finally {
    //     this.isBusy = false;
    // }
},
methods : {
    // fillDataSource(){
    //     let response = store.state.source.data_source
    //     for(var i = 0; i < response.data.length; i++){
    //         this.label_sources.push(response.data[i].name)
    //     }
    //     this.selectAllSource()
    //     this.allSelectedSource = true
    // },
    // fillDataObject(){
    //     let response = store.state.object.data_object
    //     for(var i = 0; i < response.data.length; i++){
    //         this.label_objects.push(response.data[i].name)
    //     }
    // },
    // selectAllSource: function() {
    //     this.userIdsSource = [];
    //     if (!this.allSelectedSource) {
    //         for (this.label_source in this.label_sources) {
    //             this.userIdsSource.push(this.label_sources[this.label_source].toString());
    //         }
    //     }
    // },
    // selectSource: function() {
    //     this.allSelectedSource = false;
    // },
    // selectAllObject: function() {
    //     this.userIdsObject = [];
    //     if (!this.allSelectedObject) {
    //         for (this.label_object in this.label_objects) {
    //             this.userIdsObject.push(this.label_objects[this.label_object].toString());
    //         }
    //     }
    // },
    // selectObject: function() {
    //     this.allSelectedObject = false;
    // },
    filterMenu(){
        this.$cookie.set('compare_start1', moment(this.rangeTgl.start).format('YYYY-MM-DD'))
        this.$cookie.set('compare_end1', moment(this.rangeTgl.end).format('YYYY-MM-DD'))
        this.$cookie.set('compare_start2', moment(this.rangeTgl2.start).format('YYYY-MM-DD'))
        this.$cookie.set('compare_end2', moment(this.rangeTgl2.end).format('YYYY-MM-DD'))
        // alert(moment(this.rangeTgl.start).format('YYYY-MM-DD') + "\n" + moment(this.rangeTgl.end).format('YYYY-MM-DD') + "\n" + moment(this.rangeTgl2.start).format('YYYY-MM-DD') + "\n" + moment(this.rangeTgl2.end).format('YYYY-MM-DD') + "\n" + this.userIdsSource + "\n" + this.userIdsSentiment + "\n" + this.userIdsObject)
        location.reload()
    },
    addDays(theDate, days) {
        return new Date(theDate.getTime() + days*24*60*60*1000);
    },
    toggleBodyClassMini(kondisi, className) {
        const el = document.body;

        if (kondisi === true) {
            el.classList.add(className);
        } else {
            el.classList.remove(className);
        }
    },
}
}
</script>
<style scoped>
    @media(min-width: 992px){
        .is_stuck{
            position: fixed; 
            width: 200px;
        }
    }
</style>