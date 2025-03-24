<template>
    <div class="page-product">
        <div class="columns">
            <!-- Product Image -->
            <div class="column is-half">
                <figure class="image product-image">
                    <img v-bind:src="product.get_image" alt="Product Image">
                </figure>
            </div>

            <!-- Info Container -->
            <div class="right-side-container">
                <div class="info-container">
                    <div class="column">
                        <h2 class="title has-text-black">{{ product.name }}</h2>

                        <p>{{ product.description }}</p>

                        <p><strong>${{ product.price }}</strong></p>

                        <div class="field has-addons mt-6">
                            <div class="control">
                                <input type="number" class="input" min="1" v-model="quantity">
                            </div>

                            <div class="control">
                                <a class="button is-black" @click="addToCart">Add to cart</a>
                            </div>
                        </div>

                        <div class="container mt-2">
                            <div class="box option-box">
                                <div class="columns is-vcentered">
                                    <div class="column is-narrow">
                                        <span class="icon-text">
                                            <span class="icon">
                                                <i class="fas fa-store"></i>
                                            </span>
                                            <span>In-Store Pickup</span>
                                        </span>
                                    </div>
                                    <div class="column has-text-right free">FREE</div>
                                </div>
                                <div class="divider"></div>
                                <div class="columns is-vcentered">
                                    <div class="column is-narrow">
                                        <span class="icon-text">
                                            <span class="icon">
                                                <i class="fas fa-truck"></i>
                                            </span>
                                            <span>Worldwide Shipping</span>
                                        </span>
                                    </div>
                                    <div class="column has-text-right free">FREE</div>
                                </div>
                            </div>
                        </div>

                        <div class="container mt-5">
                            <div class="box info-box">
                                <h3 class="title is-size-4 has-text-black">Easy & Secure Payment</h3>
                                <p>We offer secure payment options, including PayPal, so you can shop with confidence.</p>

                                <h3 class="title is-size-4 has-text-black mt-4">Care Instructions</h3>
                                <ul>
                                    <li>Machine wash cold with similar colors</li>
                                    <li>Do not bleach</li>
                                    <li>Tumble dry low or hang dry for best results</li>
                                    <li>Iron on low heat if needed</li>
                                </ul>

                                <h3 class="title is-size-4 has-text-black mt-4">Hassle-Free Returns</h3>
                                <p>We stand by the quality of our products! If you're not completely satisfied, we offer free returns within 15 days of purchase—no questions asked.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'Product',
    data() {
        return {
            product: {},
            quantity: 1
        }
    },
    mounted() {
        this.getProduct()
    },
    methods: {
        async getProduct() {
            this.$store.commit('setIsLoading', true)

            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

            await axios
                .get(`/api/v1/products/${category_slug}/${product_slug}/`)
                .then(response => {
                    this.product = response.data
                    document.title = this.product.name + ' - URBANFIT'
                })
                .catch(error => {
                    console.log(error)
                })
            
            this.$store.commit('setIsLoading', false) 
        },
        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            const item = {
                product: this.product,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)

            toast({
                message: "The product was added to the cart",
                type: "is-success",
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        }
    }
}
</script>

<style scoped>
.page-product {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    justify-content: start;
    width: 100%;
}

.right-side-container{
    display: flex;
    align-items: start;
    justify-self: start;
    margin: 20px;
}
.product-image {
    max-width: 100%;
    margin: 0 auto;
}

.product-image img {
    width: 100%;
    height: auto;
}

.info-container {
    padding-right: 20px;    
    display: flex;
    flex-direction: column;
    align-items: stretch;
    justify-content: start;
}

.info-container h2{
    margin: 0;
    padding: 0;
}

.info-container p {
    margin: 5px 0;
}

.input {
    background-color: white;
    color: black;
}

p {
    color: black;
}

p strong {
    color: black;
    font-size: 1.2rem;
}

.option-box {
    border: 1px solid black;
    border-radius: 8px;
    padding: 15px;
    width: 100%;
    background-color: white;
}

.option-box:not(:last-child) {
    border-bottom: none;
}

.icon-text {
    display: flex;
    align-items: center;
    color: black;
}

.icon {
    font-size: 1.5rem;
    margin-right: 10px;
    color: black;
}

.subtitle {
    color: white;
    font-size: 0.9rem;
}

.free {
    color: #009a64;
    font-weight: bold;
}

.divider {
    border-top: 1px solid black;
    margin-bottom: 20px;
}

.info-box {
    border: 1px solid black;
    border-radius: 8px;
    padding: 15px;
    background-color: white;
}

.info-box h3 {
    margin-bottom: 10px;
}

.info-box ul {
    list-style-type: disc;
    margin-left: 20px;
    color: black;
}

@media (max-width: 800px){
    .info-container{
        margin-left: 20px;
        margin-bottom: 20px;
    }
}
</style>