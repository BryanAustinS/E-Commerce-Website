<template>
    <div class="container has-text-black">
        <div class="image">
            <img :src="item.product.get_image" alt="Product Image">
        </div>

        <div class="info has-text-black">
            <div class="left">
                <div class="product-info">
                    <h2 >{{ item.product.name }}</h2>
                    <p><strong>${{ item.product.price }}</strong></p>
                </div>
                <div class="quantity">
                    <a @click="decrementQuantity(item)">-</a>
                    {{ item.quantity }}
                    <a @click="incrementQuantity(item)">+</a>
                </div>
                <p>Total: ${{ getItemTotal(item).toFixed(2) }}</p>
            </div>
            <div class="right">
                <button class="delete" @click="removeFromCart(item)"></button>
            </div>
        </div>
    </div>
    
</template>

<script>
export default {
    name: 'CartItem',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        decrementQuantity(item) {
            item.quantity -= 1

            if (item.quantity === 0) {
                this.$emit('removeFromCart', item)
            }

            this.updateCart()
        },
        incrementQuantity(item) {
            item.quantity += 1

            this.updateCart()
        },
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        removeFromCart(item) {
            this.$emit('removeFromCart', item)

            this.updateCart()
        },
    },
}
</script>

<style scoped>
.container{
    display: flex;
    background-color: #f9f9f9;
    width: 100%;
}

.image {
    flex: 1;
}

.info {
    padding-left: 20px;
    flex: 2;
}

.image img {
    max-height: 300px;
    width: auto;
}

.product-info strong {
    color: black;
}

h2 p {
    color: black;
}

.info{
    display: flex;
    background-color: #f9f9f9;
    width: 100%;
}

.left{
    flex: 1;
}

.right{
    display: flex;
    flex: 1;
    justify-content: end;
    align-items: start;
    margin-top: 20px;
    margin-right: 10px;
}

</style>
