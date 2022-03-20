<template>
<div style="padding-top: 20px">
    <div class="row">
        <div class="col-12 col-md-12 col-lg-12">
            <div class="card">
                <div class="card-header">
                    <h4>Trend Analysis</h4>
                </div>
                <div class="card-body">
                    <vue-frappe v-if="success === true"
                        id="test"
                        :labels="label"
                        type="axis-mixed"
                        :height="300"
                        :colors="['#003777']"
                        :dataSets="this.data">
                    </vue-frappe>
                </div>
            </div>        
        </div>
    </div>
</div>
</template>
<script>
import axios from 'axios'
    export default {
        data () {
            return {
                success: false,
                label: [],
                banks: ['ANZ','BCA'],
                data: [
                {
                    name: "ANZ", chartType: 'line',
                    values: []
                },
                {
                    name: "BCA", chartType: 'line',
                    values: []
                }
                ]
            }
        },
        mounted() {
            this.fillData()
        },
        methods: {
            async fillData () {
                axios.get('https://api.worldbank.org/v2/countries/NOR/indicators/NY.GDP.MKTP.KD.ZG?per_page=12&MRV=30&format=json').then(response1 => {
                    // this.data[0].name = response.data[1][0].indicator.value
                    this.data[0].name = this.banks[0]
                    for(var i = response1.data[0].per_page-1; i >= 0; i--){
                    this.data[0].values.push(response1.data[1][i].value)
                    this.label.push(response1.data[1][i].date)
                    axios.get('https://api.worldbank.org/v2/countries/NOR/indicators/SL.AGR.EMPL.ZS?per_page=12&MRV=30&format=json').then(response2 => {
                        //this.data[1].name = response.data[1][0].indicator.value
                        this.data[1].name = this.banks[1]
                        for(var i = response2.data[0].per_page-1; i >= 0; i--){
                        this.data[1].values.push(response2.data[1][i].value)
                        this.success = true
                        }
                    })
                    }
                })
            }
        },
    }
</script>