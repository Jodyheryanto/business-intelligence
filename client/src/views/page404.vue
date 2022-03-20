<template>
<div>
    <section class="section">
    <div class="container mt-5">
        <div class="page-error">
            <div class="page-inner">
                <h1>404</h1>
                <div class="page-description">
                    The page you were looking for could not be found.
                </div>
                <div class="mt-3">
                    <a href="#" @click.prevent="goBack">Back to Home</a>
                </div>
            </div>
        </div>
        <div class="simple-footer mt-5">
            Copyright &copy; Jody 2020
        </div>
    </div>
</section>
</div>
</template>
<script>
export default {
    methods: {
        goBack(){
            this.$router.replace({
                name: 'Auth'
            })
        }
    }
}
</script>