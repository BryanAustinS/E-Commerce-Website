<template>
    <div class="page-cart">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title has-text-black">SHOPPING BAG</h1>
            </div>

            <!-- Cart Table -->
            <div class="container">
                <div class="column is-12 cart-table">
                    <div class="table is-fullwidth" v-if="cartTotalLength">


                            <CartItem
                                v-for="item in cart.items"
                                v-bind:key="item.product.id"
                                v-bind:initialItem="item"
                                v-on:removeFromCart="removeFromCart" />
                    </div>

                    <p class="has-text-black" v-else>You don't have any products in your cart...</p>
                </div>

                <!-- Summary Table -->
                <div class="column is-12 summary-table">
                    <div class="text">
                        <h2 class="subtitle has-text-black">Summary</h2>

                        <strong>${{ cartTotalPrice.toFixed(2) }}</strong>, {{ cartTotalLength }} items
                    </div>
                    <router-link to="/cart/checkout" class="button has-background-black">Proceed to checkout</router-link>
                </div>
            </div>  
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import CartItem from '@/components/CartItem.vue'

export default {
    name: 'Cart',
    components: {
        CartItem
    },
    data() {
        return {
            cart: {
                items: []
            }
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
    },
    methods: {
        removeFromCart(item) {
            this.cart.items = this.cart.items.filter(i => i.product.id !== item.product.id)
        }
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
    }
}
</script>

<style scoped>
.title {
    font-size: 2.5rem;}
.container {
    display: flex;
    width: 100%;
}


.page-cart {
    padding: 20px;
    min-height: 500px;
    margin-left: 15%;
    margin-right: 15%;
}

.cart-table {
    background-color: #f9f9f9;
    margin-right: 20px;
    padding-bottom: 20px;
    padding-right: 20px;
    flex: 3;
}

.summary-table {
    background-color: #f9f9f9;
    display: flex;
    flex-direction: column;
    padding-bottom: 20px;
    padding-right: 20px;
    flex: 1;
}

strong { 
    color: black;
}

thead{
    background-color: #f9f9f9;
}

tr th{
    color: black;
}

.text {
    margin-bottom: 20px;
}

</style>