<template>
<modal 
    name="filter-data"
    transition="nice-modal-fade"
    height="auto" 
    :scrollable="true"
    :delay="100"
    :adaptive="true">
    <div class="example-modal-content">
        <h3 style="margin: 15px 20px;">Cek Laporan</h3>
        <hr>
        <p v-if="errors.length" style="margin-left: 25px;">
            <b>Please correct the following error(s):</b>
            <b v-for="(error,index) in errors" v-bind:key="index" style="color: red;"> {{ error }},</b><b style="color: red;"> Required</b>
        </p>
        <br>
        <ul type="none" style="padding-left: 40px;">
            <li>
                <div class="form-group">
                    <label for="dari_tgl">Dari Tanggal : </label>
                    <input type="date" class="form-control" name="dari_tgl" ref="dari_tgl" style="width: 90%;" v-model="form.dari_tgl">
                </div>
            </li>
            <li>
                <div class="form-group" style="margin-top: -20px;">
                    <label for="smp_tgl">Sampai Tanggal : </label>
                    <input type="date" class="form-control" name="smp_tgl" ref="smp_tgl" style="width: 90%;" v-model="form.smp_tgl">
                </div>
            </li>
        </ul>
        <footer class="modal-footer" style="margin-top: -20px">
            <slot name="footer">
            <button v-on:click="checkForm" class="btn-blue" style="margin: 0px 30px; padding: 10px;">Cek !</button>
            </slot>
        </footer>
    </div>
</modal>
</template>
<script>
import moment from 'moment';
export default {
    data() {
        return {
            form: {
                dari_tgl: null,
                smp_tgl: null
            },
            errors:[],
        }
    },
    methods:{
        checkForm:function(e) {
            if(this.form.dari_tgl && this.form.smp_tgl){
                moment(this.form.dari_tgl, 'YYYY-MM-DD').format('YYYY-MM-DD hh:mm:ss')
                moment(this.form.smp_tgl, 'YYYY-MM-DD').format('YYYY-MM-DD hh:mm:ss')
                this.submitForm();
            }
            this.errors = [];
            if(!this.form.dari_tgl) this.errors.push("Dari Tanggal");
            if(!this.form.smp_tgl) this.errors.push("Sampai Tanggal");
            e.preventDefault();
        },
        close() {
        this.$emit('close');
        },
        submitForm(){
            this.$cookie.set('dari_tgl', this.form.dari_tgl)
            this.$cookie.set('smp_tgl', this.form.smp_tgl)
            this.$router.replace({
                name: 'ReportReviews'
            })
        }
    }
}
</script>

<style scope>
    li{
    padding-bottom: 10px;
    }
    .modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
    }

    .modal {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
    }

    .modal-header,
    .modal-footer {
    padding: 15px;
    display: flex;
    }

    .modal-header {
    border-bottom: 1px solid #eeeeee;
    color: #4AAE9B;
    justify-content: space-between;
    }

    .modal-footer {
    border-top: 1px solid #eeeeee;
    justify-content: flex-end;
    }

    .modal-body {
    position: relative;
    padding-right: 30px;
    padding-top: 10px;
    }

    .btn-close {
    border: none;
    font-size: 20px;
    cursor: pointer;
    font-weight: bold;
    color: #4AAE9B;
    background: transparent;
    }

    .btn-blue {
    color: white;
    font-weight: bold;
    font-size: 13px;
    background: #0044ff;
    border: 1px solid #4AAE9B;
    border-radius: 5px;
    padding: 5px;
    }

    .btn-green {
    color: white;
    font-weight: bold;
    font-size: 13px;
    background: #22ff00;
    border: 1px solid #4AAE9B;
    border-radius: 5px;
    padding: 5px;
    }

    .btn-red {
    margin-left: 2px;
    color: white;
    font-weight: bold;
    font-size: 13px;
    background: red;
    border-radius: 5px;
    padding: 5px;
    }
</style>