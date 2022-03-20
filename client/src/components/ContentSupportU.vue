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

            <app-table-help-user></app-table-help-user>
            <app-table-notif-user></app-table-notif-user>

        </section>
    </div>
</template>
<script>
// import ChartLine from './ChartLine.vue'
// import ChartBar from './ChartBar.vue'
//import TableInsight from './TableInsight.vue'
// import TableComment from './TableComment.vue'
import HelpUsers from './TableHelpUsers.vue'
import NotifUsers from './TableNotifUsers.vue'
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
        'app-table-help-user': HelpUsers,
        'app-table-notif-user': NotifUsers,
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