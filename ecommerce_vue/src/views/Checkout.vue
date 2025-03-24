<template>
    <div class="page-checkout">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>

            <div class="summary-container column is-12 box">
                <h2 class="subtitle has-text-black">SUMMARY</h2>
                <div class="summary-content">
                    <div class="left has-text-black">
                        <h3>Order value: </h3>
                        <h3>Shipping fee: </h3>
                        <div class="separator"></div>
                        <h3>Total: </h3>
                    </div>

                    <div class="right">
                        <h3>${{ cartTotalPrice.toFixed(2) }}</h3>
                        <h3>$0.00</h3>
                        <div class="separator"></div>
                        <h3>${{ cartTotalPrice.toFixed(2) }}</h3>
                    </div>
                </div>

            </div>

            <div class="column is-12 box">
                <h2 class="subtitle has-text-black">Shipping details</h2>
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

                <template v-if="cartTotalLength">
                    <div id="paypal-button-container">
                        <button class="paypal-button" @click="submitForm">                            
                            <img src="@/assets/pngegg.png" alt="PayPal Logo" class="paypal-logo">
                        </button>
                    </div>
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
        document.title = "Checkout - URBANFIT";
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


<style scoped>
.page-checkout {
    padding: 20px;
    margin-left: 15%;
    margin-right: 15%;
}

.title{
    font-size: 2.5rem;
    color: black;
}

.box {
    background-color: #f9f9f9;
    border-radius: 0;
}

label {
    color: black;
}

input { 
    background-color: white;
    border: 0px solid #f9f9f91e;
    color: black;
}

#paypal-button-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
}

/* PayPal Button Styles */
.paypal-button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background-color: #ffc439; /* PayPal yellow */
    border: none;
    border-radius: 6px; /* Rounded corners */
    padding: 10px 20px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2); /* Add subtle shadow */
}

.paypal-button:hover {
    background-color: #ffb347; /* Slightly darker yellow on hover */
}

/* PayPal Logo */
.paypal-logo {
    height: 24px; /* Adjust the height of the logo */
    width: auto; /* Maintain aspect ratio */
}

.summary-content{
    display: flex;
    flex-direction: row;
}

.left {
    display: flex;
    flex-direction: column;
    align-items: start;
    margin-right: 20px;
    flex: 1;
}

.right {
    display: flex;
    flex-direction: column;
    align-items: start;
    margin-right: 20px;
    flex: 4;
}

.right h3{
    color: black;
    font-weight: bold;
}

.separator{
    border-top: 1px solid #333;
    padding-top: 20px;
    padding-bottom: 10px;
}
    
</style>