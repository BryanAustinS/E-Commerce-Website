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
    width: 100%;
    margin-left: 10px;
    text-decoration: none; /* Remove underline for the link */
    color: inherit; /* Inherit text color */
    cursor: pointer; /* Show pointer cursor on hover */
    transition: transform 0.2s ease; /* Add hover effect */
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
}

.product-price {
    font-size: 14px;
    color: grey;
}
</style>