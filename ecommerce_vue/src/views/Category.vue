<template>
  <div class="page-category">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered has-text-black">{{ category.name }}</h2>
      </div>

      <!-- Product rows -->
      <div class="product-row">
        <ProductBox
          v-for="product in category.products"
          v-bind:key="product.id"
          v-bind:product="product"
          class="product-box"
        ></ProductBox>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast';
import ProductBox from '@/components/ProductBox.vue';

export default {
  name: 'Category',
  components: {
    ProductBox,
  },
  data() {
    return {
      category: {},
      products: [],
    };
  },
  mounted() {
    this.getCategory();
  },
  watch: {
    $route(to, from) {
      // Enable us to change between categories
      this.getCategory();
    },
  },
  methods: {
    async getCategory() {
      const categorySlug = this.$route.params.category_slug;
      this.$store.commit('setIsLoading', true);
      await axios
        .get(`/api/v1/products/${categorySlug}/`)
        .then((response) => {
          this.category = response.data;
          document.title = this.category.name + ' - Ecommerce';
        })
        .catch((error) => {
          console.log(error);
          toast({
            message: 'Something went wrong. Please try again',
            type: 'is-danger',
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: 'bottom-right',
          });
        });
      this.$store.commit('setIsLoading', false);
    },
  },
};
</script>

<style scoped>
.page-category {
  padding: 20px;
}

.product-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start; /* Align items to the start */
  gap: 10px; /* Reduce the gap between product boxes */
}

.product-box {
  width: 160px; /* Ensure consistent width */
  box-sizing: border-box;
}
</style>