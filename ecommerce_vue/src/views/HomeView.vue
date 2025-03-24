<template>
  <div class="home">
    <section class="hero is-small">
      <figure class="image hero-image">
        <img src="@/assets/hero_bg2.jpg" alt="Hero Background">
        <div class="hero-text">
          <p class="subtitle is-size-3">Welcome to</p>
          <p class="title is-size-1">URBANFIT</p>
        </div>
      </figure>
    </section>

    <div class="columns mt-3 is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-left has-text-black">Latest Products</h2>
      </div>

      <div class="product-row">
        <ProductBox
          v-for="product in latestProducts"
          v-bind:key="product.id"
          v-bind:product="product"
          class="product-box"
        ></ProductBox>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';
import ProductBox from '@/components/ProductBox.vue';

export default {
  name: 'HomeView',
  data() {
    return {
      latestProducts: []
    };
  },
  components: {
    ProductBox,
  },
  mounted() {
    this.getLatestProducts();
    document.title = 'Home - URBANFIT';
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true);

      await axios
        .get('/api/v1/latest-products/')
        .then(response => {
          this.latestProducts = response.data;
        })
        .catch(error => console.error(error));

      this.$store.commit('setIsLoading', false);
    }
  }
};
</script>

<style scoped>
.home {
  min-height: 1000px;
  padding-left: 20px;
  padding-right: 20px;
}

.hero {
  width: 100vw;
  margin-left: calc(-50vw + 50%);
  margin-top: 0;
  height: 500px;
  position: relative;
  overflow: hidden;
  align-items: center;
  justify-content: center;
}

.hero-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}

.hero-text .subtitle {
  font-size: 1.5rem;
  color: white;
  font-family: 'Bebas Neue', sans-serif;
  letter-spacing: 1px; 
}

.hero-text .title {
  font-size: 2.5rem;
  color: white;
  font-family: 'Bebas Neue', sans-serif;
  letter-spacing: 1px; 
}

/* Product row styling */
.product-row {
  display: flex;
  flex-wrap: wrap; 
  justify-content: space-between;
}

.product-box {
  flex: 1 1 calc(25% - 20px); 
  max-width: calc(25% - 20px); 
  box-sizing: border-box; 
  margin-left: 20px;
}

@media (max-width:800px){
  .hero{
    display: flex;
    align-items: stretch;
  }
}
</style>