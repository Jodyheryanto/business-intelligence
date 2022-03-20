<template>
<div class="row">
    <div class="col-12 col-md-12 col-lg-12">
        <div class="card">
            <div class="card-header">
                <h4>Sentiments History</h4>
            </div>
            <div class="card-body" style="text-align: center">
                <apexchart v-if="length !== 0" class="chart" type="line" height="350" style="padding: 10px;" :options="chartOptions" :series="series"></apexchart>
                <h4 style="color: red; margin-top: 20px;" v-else>Data tidak ada</h4>
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
                // {
                //     name: "Neutral Reviews",
                //     data: []
                // },
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
    mounted() {
        this.fillData()
    },
    methods: {
        fillData () {
            let data = store.state.post.DataPostFilter
            this.length = store.state.post.DataPostFilter.length
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
            // moment(date, 'YYYYMM').format('MMMM YYYY')
            // console.log(this.temps)
            // i = 0;
            // while(i < this.temps.length){
            //     for(var j = 0; j < this.temps.length; j++){
            //         if(this.temps[i].month !== this.temps.month[j]){
            //             this.chartOptions.xaxis.categories.push(this.temps[i].month)
            //         }
            //     }
            // }
            // console.log(this.chartOptions.xaxis.categories)
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
                        }// else if(this.temps[j].sentiment === 1){
                        //     neu += 1
                        //     temp += 1
                        // }
                        else{
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
            // console.log(this.series[0].data)
            this.success = true 
        },
        // async fillData () {
        //     axios.get('https://api.worldbank.org/v2/countries/NOR/indicators/NY.GDP.MKTP.KD.ZG?per_page=12&MRV=30&format=json').then(response1 => {
        //         this.series[0].name = response1.data[1][0].indicator.value
        //         for(var i = response1.data[0].per_page-1; i >= 0; i--){
        //         this.series[0].data.push(response1.data[1][i].value)
        //         this.chartOptions.xaxis.categories.push(response1.data[1][i].date)
        //         }
        //         axios.get('https://api.worldbank.org/v2/countries/NOR/indicators/SL.AGR.EMPL.ZS?per_page=12&MRV=30&format=json').then(response2 => {
        //             this.series[1].name = response2.data[1][0].indicator.value
        //             for(var i = response2.data[0].per_page-1; i >= 0; i--){
        //                 this.series[1].data.push(response2.data[1][i].value)
        //             }
        //             this.success = true
        //         })
        //     })
        // }
    },
}
</script>
