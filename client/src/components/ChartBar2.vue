<template>
    <div class="col-12 col-md-6 col-lg-6">
        <div class="card">
            <div class="card-header">
                <div>
                    <h4>Score Board</h4>
                    <ul class="nav card-header-tabs pull-right"  id="myTab" role="tablist">
                        <li class="nav-item">
                        <a class="nav-link active" id="home-tab" data-toggle="tab" href="#home" role="tab" aria-controls="home" aria-selected="true"><strong>Buzz</strong></a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" id="profile-tab" data-toggle="tab" href="#profile" role="tab" aria-controls="profile" aria-selected="false">Facebook</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" id="contact-tab" data-toggle="tab" href="#contact" role="tab" aria-controls="contact" aria-selected="false">Twitter</a>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="card-body">
                <vue-frappe v-if="success === true"
                    id="coba"
                    :labels="label"
                    type="axis-mixed"
                    :height="370"
                    :colors="['#003777']"
                    :dataSets="this.data">
                </vue-frappe>
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
                label: ['ANZ','BCA', 'BNI', 'BRI', 'BTN', 'BTPN', 'Citi', 'DBS', 'HSBC', 'Permata'],
                data: [
                {
                    name: this.label, chartType: 'bar',
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
                axios.get('https://api.worldbank.org/v2/countries/NOR/indicators/NY.GDP.MKTP.KD.ZG?per_page=10&MRV=30&format=json').then(response => {
                    //this.data[0].name = response.data[1][0].indicator.value
                    for(var i = response.data[0].per_page-1; i >= 0; i--){
                    this.data[0].values.push(response.data[1][i].value)
                    //this.label.push(response.data[1][0].indicator.value)
                    }
                    this.success = true
                    // this.income = incomeresult
                    // this.date = dateresult
                })
                .catch(error => {
                    console.log(error)
                })
            }
        },
    }
</script>