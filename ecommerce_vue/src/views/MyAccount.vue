<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title has-text-black">My account</h1>
            </div>

            <hr>

            <div class="column is-12">
                <h2 class="subtitle has-text-black">My orders</h2>

                <p class="has-text-grey" v-if="orders.length === 0">You have no orders yet.</p>

                <OrderSummary v-else
                    v-for="order in orders"
                    v-bind:key="order.id"
                    v-bind:order="order" />
            </div>

            <div class="column is-12">
                <button @click="logout()" class="button is-black">Log out</button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import OrderSummary from '@/components/OrderSummary.vue'

export default {
    name: 'MyAccount',
    components: {
        OrderSummary
    },
    data() {
        return {
            orders: []
        }
    },
    mounted() {
        document.title = 'My account | URBANFIT'

        this.getMyOrders()
    },
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")

            this.$store.commit('removeToken')

            this.$router.push('/')
        },
        async getMyOrders() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get('/api/v1/orders/')
                .then(response => {
                    this.orders = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>

<style scoped>
.page-my-account {
    padding: 20px;
    min-height: 500px;
    margin-left: 15%;
    margin-right: 15%;
}

.title {
    font-size: 2.5rem;
}
</style>