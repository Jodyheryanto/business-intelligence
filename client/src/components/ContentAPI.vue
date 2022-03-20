<template>
    <div class="main-content">
        <section class="section">
            <!-- <app-chart-line></app-chart-line>

            <div class="row">
                <app-chart-bar></app-chart-bar>
                <app-word-cloud></app-word-cloud>
            </div> -->

            <!-- <demo-draggable-modal/> -->
            <filter-data/>
            <modal-ubah/>
            <!-- <app-table-insight></app-table-insight> -->

            <!-- <app-table-comment></app-table-comment> -->

            <app-table-api></app-table-api>

        </section>
    </div>
</template>
<script>
// import ChartLine from './ChartLine.vue'
// import ChartBar from './ChartBar.vue'
//import TableInsight from './TableInsight.vue'
// import TableComment from './TableComment.vue'
import TableAPI from './TableAPI.vue'
// import WordCloud from './WordCloud.vue'
// import DemoDraggableModal  from './detailWordCloud.vue'
import FilterDate from './FilterDate.vue'
import ubahUser from './Ubah.vue'
export default {
    components: {
        // 'app-chart-line': ChartLine,
        // 'app-chart-bar': ChartBar,
        //'app-table-insight': TableInsight,
        // 'app-table-comment': TableComment,
        'app-table-api': TableAPI,
        // 'app-word-cloud': WordCloud,
        'filter-data': FilterDate,
        'modal-ubah': ubahUser,
        // DemoDraggableModal
    },
}
</script>
<style>
.main-content{
    min-height: 700px;
}
</style>