<template>
    <router-link :to="product.get_absolute_url" class="product-box">
        <figure class="product-image">
            <img :src="product.get_thumbnail" alt="Product Image">
        </figure>

        <div class="product-details">
            <h3 class="product-name">{{ product.name }}</h3>
            <p class="product-price">€{{ product.price }}</p>
        </div>
    </router-link>
</template>

<script>
export default {
    name: 'ProductBox',
    props: {
        product: Object
    }
}
</script>

<style scoped>
.product-box {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 160px;
    margin-left: 10px;
    text-decoration: none;
    color: inherit;
    cursor: pointer; 
    transition: transform 0.2s ease;
    margin-bottom: 30px;

}

.product-box:hover {
    transform: scale(1.02); /* Slightly enlarge the box on hover */
}

.product-image img {
    width: 100%;
    height: auto;
}

.product-details {
    margin-top: 5px;
    text-align: left;
}

.product-name {
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 2px;
    color: black;
}

.product-price {
    font-size: 14px;
    color: black;
}
</style>