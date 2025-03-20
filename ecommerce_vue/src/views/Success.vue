<template>
    <div class="page-success">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Success</h1>

                <p>Your order will be processed within 48 hours</p>
            </div>
        </div>
    </div>

</template>

<script>
export default {
    name: 'Success',
    mounted() {
        document.title = 'Success | Ecommerce'
        
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