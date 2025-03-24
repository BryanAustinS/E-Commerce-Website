<template>
    <div class="page-success">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Success</h1>

                <p>Your order will be processed within 48 hours</p>
            </div>

            <router-link to="/my-account" class="button has-background-black">Back to Home</router-link>
        </div>
    </div>

</template>

<script>
export default {
    name: 'Success',
    mounted() {
        document.title = 'Success - URBANFIT'
        
        const paymentID = this.$route.query.paymentId
        const payerID = this.$route.query.PayerID
        
        if (paymentID && payerID) {
            this.$store.commit('setIsLoading', true)
            
            axios.post('/api/v1/paypal-execute-payment/', {
                paymentID: paymentID,
                payerID: payerID
            })
            .then(() => {
                this.$store.commit('clearCart')
                this.$store.commit('setIsLoading', false)
            })
            .catch(error => {
                console.log(error)
                this.$store.commit('setIsLoading', false)
            })
        }
    }
}
</script>

<style scoped>
.page-success {
    padding: 20px;
    height: 500px;
    margin-left: 15%;
    margin-right: 15%;
}
.title {
    font-size: 2.5rem;
    color: black;
}

p {
    color: black;
}

button {
    margin: 20px;
}
</style>