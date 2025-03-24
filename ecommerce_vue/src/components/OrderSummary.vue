<template>
    <div class="box mb-4 cart-box">
        <h3 class="title is-size-6 mb-4 has-text-black">Order ID: {{ order.id }}</h3>

        <div class="summary-container" 
            v-for="item in order.items"
            v-bind:key="item.product.id"
        >
            <div class="product-container">
                <div class="image">
                    <img :src="item.product.get_image" alt="Product Image">
                </div>

                <div class="info has-text-black">
                    <div class="left">
                        <div class="product-info">
                            <h2>{{ item.product.name }}</h2>
                            <p><strong>${{ item.price }}</strong></p>
                        </div>
                        <div class="quantity">
                            Quantity: {{ item.quantity }}
                        </div>
                    </div>
                </div>
            </div>
            <div class="summary-info">
                <p class="has-text-black">Total: ${{ getItemTotal(item).toFixed(2) }}</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'OrderSummary',
    props: {
        order: Object
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.price
        },
        orderTotalLength(order) {
            return order.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
    }
}
</script>

<style scoped>
.cart-box {
    padding: 20px;
    border-radius: 0px;
    background-color: #f9f9f9;
}

.summary-container{
    display: flex;
    flex-direction: row;
}


.product-container{
    display: flex;
    flex: 3;
}

.summary-info{
    display: flex;
    flex: 1;
}

.image img {
    max-height: 150px;
    width: auto;
}

.info{
    padding-left: 20px;
}

.info strong {
    color: black;
}
</style>