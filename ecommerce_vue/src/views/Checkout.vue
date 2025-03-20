<template>
    <div class="page-checkout">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>

            <div class="column is-12 box">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="item in cart.items"
                            :key="item.product.id">
                                <td>{{ item.product.name }}</td>
                                <td>${{ item.product.price }}</td>
                                <td>{{ item.quantity }}</td>
                                <td>${{ getItemTotal(item) }}</td>
                        </tr>
                    </tbody>

                    <tfoot>
                        <tr>
                            <td colspan="2">Total</td>
                            <td>{{ cartTotalLength }}</td>
                            <td>${{ cartTotalPrice }}</td>
                        </tr>
                    </tfoot>
                </table>
            </div>

            <div class="column is-12 box">
                <h2 class="subtitle">Shipping details</h2>
                <p class="has-text-grey mb-4">* All fields are required</p>
                
                <div class="columns is-multiline">
                    <div class="column is-6">
                        <div class="field">
                            <label class="label">First Name*</label>
                            <div class="control">
                                <input class="input" type="text" v-model="first_name">
                            </div>
                        </div>

                        <div class="field">
                            <label class="label">Last Name*</label>
                            <div class="control">
                                <input class="input" type="text" v-model="last_name">
                            </div>
                        </div>

                        <div class="field">
                            <label class="label">E-mail*</label>
                            <div class="control">
                                <input class="input" type="text" v-model="email">
                            </div>
                        </div>

                        <div class="field">
                            <label class="label">Phone*</label>
                            <div class="control">
                                <input class="input" type="text" v-model="phone">
                            </div>
                        </div>
                    </div>

                        
                    <div class="column is-6">
                        <div class="field">
                            <label class="label">Address*</label>
                            <div class="control">
                                <input class="input" type="text" v-model="address">
                            </div>
                        </div>

                        <div class="field">
                            <label class="label">Zip code*</label>
                            <div class="control">
                                <input class="input" type="text" v-model="zipcode">
                            </div>
                        </div>

                        <div class="field">
                            <label class="label">Place*</label>
                            <div class="control">
                                <input class="input" type="text" v-model="place">
                            </div>
                        </div>
                    </div>
                </div>
            <div class="notification is-danger mt-4" v-if="errors.length">
                    <p v-for="error in errors" :key="error">{{ error }}</p>
                </div>

                <hr>

                <div id="card-element" class="mb-5"></div>

                <template v-if="cartTotalLength">
                    <hr>

                    <button class="button is-dark" @click="submitForm">Pay</button>
                </template>
            </div>


        </div>
    </div>

</template>

<script>
import axios from 'axios'

export default {
    name: "Checkout",
    data() {
        return {
        cart: {
            items: []
        }, 
        stripe: {},
        card: {},
        first_name: "",
        last_name:  "",
        email: "",
        phone: "",
        address: "",
        zipcode: "",
        place: "",
        errors: []
        }
    },
    mounted() {
        document.title = "Checkout - Ecommerce";
        this.cart = this.$store.state.cart;
    },
    methods: {
        getItemTotal(item){
            return item.quantity * item.product.price;
        },
        submitForm(){
            this.errors = []

            if (this.first_name === "") {
                this.errors.push("First name is required")
            }
            if (this.last_name === "") {
                this.errors.push("Last name is required")
            }
            if (this.email === "") {
                this.errors.push("Email is required")
            }
            if (this.phone === "") {
                this.errors.push("Phone is required")
            }
            if (this.address === "") {
                this.errors.push("Address is required")
            }
            if (this.zipcode === "") {
                this.errors.push("Zip code is required")
            }
            if (this.place === "") {
                this.errors.push("Place is required")
            }
            if (!this.errors.length) {
                this.$store.commit('setIsLoading', true)
        
                // Create order items from cart
                const items = this.cart.items.map(item => ({
                    product: item.product.id,
                    price: item.product.price,
                    quantity: item.quantity
                }))
                
                // Create the order
                const orderData = {
                    first_name: this.first_name,
                    last_name: this.last_name,
                    email: this.email,
                    phone: this.phone,
                    address: this.address,
                    zipcode: this.zipcode,
                    place: this.place,
                    items: items
                }
                
                axios.post('/api/v1/checkout/', orderData)
                    .then(response => {
                        this.orderId = response.data.id
                        this.initiatePayPal(this.orderId)
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                        } else {
                            this.errors.push('Something went wrong. Please try again!')
                        }
                        this.$store.commit('setIsLoading', false)
                    })
                    }
        },
        initiatePayPal(orderId) {
            axios.post('/api/v1/paypal-create-payment/', { order_id: orderId })
                .then(response => {
                    window.location.href = response.data.approval_url
                })
                .catch(error => {
                    this.errors.push('Payment processing error. Please try again.')
                    this.$store.commit('setIsLoading', false)
        })
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