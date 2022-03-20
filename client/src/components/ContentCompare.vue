<template>
    <div class="main-content">
        <section class="section">
            <compare-list></compare-list>

            <div class="row">
                <div class="col-12 col-md-12 col-lg-12">
                    <div class="card">
                        <div class="card-header d-block text-center">
                            <h4>-- Sentiment History Versus --</h4>
                        </div>
                    </div>        
                </div>
            </div>

            <div class="row">
                <div class="col-12 col-lg-6"><app-chart-line1></app-chart-line1></div>
                <div class="col-12 col-lg-6"><app-chart-line2></app-chart-line2></div>
            </div>

            <!-- <div class="row">
                <app-chart-bar></app-chart-bar>
                <app-chart-bar></app-chart-bar>
                <app-word-cloud></app-word-cloud>
            </div> -->

            <demo-draggable-modal/>
            <filter-data/>
            <versus-date/>
            <!-- <app-table-insight></app-table-insight> -->
            <div class="row">
                <div class="col-12 col-md-12 col-lg-12">
                    <div class="card">
                        <div class="card-header d-block text-center">
                            <h4>-- Post Count By User Versus --</h4>
                        </div>
                    </div>        
                </div>
            </div>
            <div class="row">
                <app-table-comment1 class="col-12 col-lg-6"></app-table-comment1>
                <app-table-comment2 class="col-12 col-lg-6"></app-table-comment2>
            </div>

            <div class="row">
                <div class="col-12 col-md-12 col-lg-12">
                    <div class="card">
                        <div class="card-header d-block text-center">
                            <h4>-- Post Data Versus --</h4>
                        </div>
                    </div>        
                </div>
            </div>

            <div class="row">
                <app-table-post1 class="col-12 col-lg-6"></app-table-post1>
                <app-table-post2 class="col-12 col-lg-6"></app-table-post2>
            </div>
            

        </section>
    </div>
</template>
<script>
import ChartLine1 from './CompareChartLine1.vue'
import ChartLine2 from './CompareChartLine2.vue'
// import ChartBar from './ChartBar.vue'
//import TableInsight from './TableInsight.vue'
import TableComment1 from './CompareTableComment1.vue'
import TableComment2 from './CompareTableComment2.vue'
import TablePost1 from './CompareTablePost1.vue'
import TablePost2 from './CompareTablePost2.vue'
// import WordCloud from './WordCloud.vue'
import CompareList from './CompareList.vue'
import DemoDraggableModal  from './detailWordCloud.vue'
import FilterDate from './FilterDate.vue'
import VersusDate from './VersusDate.vue'
export default {
    components: {
        'app-chart-line1': ChartLine1,
        'app-chart-line2': ChartLine2,
        // 'app-chart-bar': ChartBar,
        //'app-table-insight': TableInsight,
        'app-table-comment1': TableComment1,
        'app-table-comment2': TableComment2,
        'app-table-post1': TablePost1,
        'app-table-post2': TablePost2,
        // 'app-word-cloud': WordCloud,
        'filter-data': FilterDate,
        'versus-date': VersusDate,
        'compare-list': CompareList,
        DemoDraggableModal
    },
    data(){
        return{
        }
    }
}
</script>
<style>
.main-content{
    min-height: 700px;
}
</style>