<template>
<div class="row">
    <div class="col-12 col-md-12 col-lg-12">
        <div class="card">
            <div class="card-header">
                <h4>Sentiments History</h4>
            </div>
            <div class="card-body">
                <apexchart v-if="length != 0" class="chart" type="line" height="350" style="padding: 10px;" :options="chartOptions" :series="series"></apexchart>
                <h4 style="color: red; margin-top: 20px; height: 340px;" class="text-center" v-else>Data tidak ada</h4>
            </div>
        </div>        
    </div>
</div>
</template>

<script>
// @ is an alias to /src
import VueApexCharts from 'vue-apexcharts'
import store from '@/store'
import moment from 'moment';
export default {
components: {
'apexchart': VueApexCharts,
},
    data() {
        return{
            success: false,
            temps: [],
            date_temps: [],
            aplikasi: '',
            length: 0,
            series: [
                {
                    name: "Posts Total",
                    data: []
                },
                {
                    name: "Positive Reviews",
                    data: []
                },
                {
                    name: "Negative Reviews",
                    data: []
                }
            ],
            chartOptions: {
                chart: {
                    type: 'area',
                    stacked: false,
                    height: 350,
                    zoom: {
                    type: 'x',
                    enabled: true,
                    autoScaleYaxis: true
                    },
                    toolbar: {
                    autoSelected: 'zoom'
                    }
                },
                dataLabels: {
                    enabled: false
                },
                markers: {
                    size: 0,
                },
                yaxis: {
                    title: {
                    text: 'Posts'
                    }
                },
                xaxis: {
                    categories: [],
                    title: {
                    text: 'Date'
                    }
                },
            }
        }
    },
    async mounted() {
        this.fillData()
    },
    methods: {
        fillData () {
            let data = store.state.post.DataCompare1
            this.length = store.state.post.DataCompare1.length
            for(var i = 0; i < data.length; i++){
                this.temps.push({date: data[i].tanggal_post, sentiment: data[i].sentiment})
            }
            if(this.date_temps.length === 0){
                this.date_temps.push(this.temps[0].date)
            }
            for(i = 0; i < this.temps.length; i++){
                var is_ava = 0
                for(var j = 0; j < this.date_temps.length; j++){
                    if(this.date_temps[j] === this.temps[i].date){
                        is_ava = 1
                    }
                }
                if(is_ava === 0){
                    this.date_temps.push(this.temps[i].date)
                }
            }
            this.date_temps.sort()
            for(i = 0; i < this.date_temps.length; i++){
                this.chartOptions.xaxis.categories.push(moment(this.date_temps[i]).format('DD MMM YYYY'))
            }
            for(i = 0; i < this.chartOptions.xaxis.categories.length; i++){
                var temp = 0
                var pos = 0
                // var neu = 0
                var neg = 0
                for(j = 0; j < this.temps.length; j++){
                    if(this.temps[j].date === moment(this.chartOptions.xaxis.categories[i]).format('YYYY-MM-DD')){
                        if(this.temps[j].sentiment === 0){
                            neg += 1
                            temp += 1
                        }else{
                            pos += 1
                            temp += 1
                        }
                    }
                }
                this.series[0].data.push(temp)
                this.series[1].data.push(pos)
                // this.series[2].data.push(neu)
                this.series[2].data.push(neg)
            }
            this.success = true 
        },
    },
}
</script>
