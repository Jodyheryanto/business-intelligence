
<template>
        <div class="col-12 col-md-6 col-lg-6">
            <div class="card">
                <div class="card-header">
                    <h4>Score Board</h4>
                </div>
                <div class="card-body text-center">
                    <apexchart v-if="length !== 0" class="chart" type="bar" height="380" style="padding: 10px;" :options="chartOptions" :series="series"></apexchart>
                </div>
            </div>        
        </div>
</template>

<script>
// @ is an alias to /src
import VueApexCharts from 'vue-apexcharts'
import store from '@/store'

export default {
    components: {
        'apexchart': VueApexCharts,
    },
    data() {
        return{
            success: false,
            length: 0,
            series: [{
                data: []
            }],
            chartOptions: {
                chart: {
                type: 'bar',
                height: 380
                },
                plotOptions: {
                bar: {
                    horizontal: true,
                }
                },
                dataLabels: {
                enabled: false
                },
                xaxis: {
                categories: [],
                }
            },
        }      
    },
    async mounted() {
        this.chartOptions.xaxis.categories = []
        var sou_length = this.$cookie.get('source_length')
        for(var i=0; i<sou_length; i++){
            this.chartOptions.xaxis.categories.push(this.$cookie.get('source'+i))
        }
        this.fillData()
    },
    methods: {
        fillData(){
            let data = store.state.post.DataPostFilter
            let items = []
            var googlePlay = 0
            var appStore = 0
            var instagram = 0
            for(var i = 0; i < data.length; i++){
                if(data[i].sumber === 'Google Play'){
                    googlePlay += 1
                }else if(data[i].sumber === 'App Store'){
                    appStore += 1
                }else if(data[i].sumber === 'Instagram'){
                    instagram += 1
                }
            }
            items.push({count: googlePlay, label: "Google Play"})
            items.push({count: appStore, label: "App Store"})
            items.push({count: instagram, label: "Instagram"})
            for(i=0; i<this.chartOptions.xaxis.categories.length; i++){
                for(var j=0;j<items.length;j++){
                    if(items[j].label === this.chartOptions.xaxis.categories[i]){
                        this.series[0].data.push(items[j].count)
                    }
                }
            }
            this.length = this.series[0].data
        }
    }
}
</script>
