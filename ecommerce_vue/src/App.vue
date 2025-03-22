<template>
  <div id="wrapper" class="has-background-white">
    <nav class="navbar has-background-white">
      <div class="navbar-brand">
        <router-link to="/men" class="navbar-item">MEN</router-link>
        <router-link to="/women" class="navbar-item">WOMEN</router-link>

        <div class="navbar-center">
          <router-link to="/" class="navbar-item"><strong>Die Mode</strong></router-link>
        </div>
      </div>



      <div class="navbar-end">
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{ 'is-active': showMobileMenu, 'has-background-white': showMobileMenu}">
        <div class="navbar-end">
          <div class="search-container">
            <form methods="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input search-input" placeholder="Search" name="query">
                </div>
                <div class="control">
                  <button type="submit" class="button search-button">
                    <span class="icon">
                      <i class="fas fa-search"></i>
                    </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
          <template v-if="$store.state.isAuthenticated">
            <router-link to="/my-account" class="navbar-item is-white">My account</router-link>
          </template>
          <template v-else>
            <router-link to="/log-in" class="navbar-item is-white">Log in</router-link>
          </template>
          <router-link to="/cart" class="navbar-item is-white">
            <span class="icon"><i class="fas fa-shopping-cart"></i></span>
            <span>Cart ({{ cartTotalLength }})</span>
          </router-link>
        </div>   
      </div>

    </nav>

    <div class="is-loading-bar has-text-centered" v-bind:class="{ 'is-loading': $store.state.isLoading }">
      <div class="lds-dual-ring"></div>
    </div>

    <section class="section">
      <router-view/>
    </section>

    <footer class="footer has-background-black">
      <div class="content has-text-centered">
        <p>
          <a href="">
            <svg class="svg-inline--fa fa-facebook-square fa-w-14 fa-2x" aria-hidden="true" data-prefix="fab" data-icon="facebook-square" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" data-fa-i2svg=""><path fill="white" d="M448 80v352c0 26.5-21.5 48-48 48h-85.3V302.8h60.6l8.7-67.6h-69.3V192c0-19.6 5.4-32.9 33.5-32.9H384V98.7c-6.2-.8-27.4-2.7-52.2-2.7-51.6 0-87 31.5-87 89.4v49.9H184v67.6h60.9V480H48c-26.5 0-48-21.5-48-48V80c0-26.5 21.5-48 48-48h352c26.5 0 48 21.5 48 48z"></path></svg>
          </a>  
          <a href="">
            <svg class="svg-inline--fa fa-twitter-square fa-w-14 fa-2x" aria-hidden="true" data-prefix="fab" data-icon="twitter-square" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" data-fa-i2svg=""><path fill="white" d="M400 32H48C21.5 32 0 53.5 0 80v352c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V80c0-26.5-21.5-48-48-48zm-48.9 158.8c.2 2.8.2 5.7.2 8.5 0 86.7-66 186.6-186.6 186.6-37.2 0-71.7-10.8-100.7-29.4 5.3.6 10.4.8 15.8.8 30.7 0 58.9-10.4 81.4-28-28.8-.6-53-19.5-61.3-45.5 10.1 1.5 19.2 1.5 29.6-1.2-30-6.1-52.5-32.5-52.5-64.4v-.8c8.7 4.9 18.9 7.9 29.6 8.3a65.447 65.447 0 0 1-29.2-54.6c0-12.2 3.2-23.4 8.9-33.1 32.3 39.8 80.8 65.8 135.2 68.6-9.3-44.5 24-80.6 64-80.6 18.9 0 35.9 7.9 47.9 20.7 14.8-2.8 29-8.3 41.6-15.8-4.9 15.2-15.2 28-28.8 36.1 13.2-1.4 26-5.1 37.8-10.2-8.9 13.1-20.1 24.7-32.9 34z"></path></svg>
          </a>
          <a href="">
            <svg class="svg-inline--fa fa-instagram fa-w-14 fa-2x" aria-hidden="true" data-prefix="fab" data-icon="instagram" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" data-fa-i2svg=""><path fill="white" d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"></path></svg>
          </a>
        </p>
      </div>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: []
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = `Token  ${token}`
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0
      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity
      }
      return totalLength
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

.navbar-burger {
  display: none;
}

@media (max-width: 1000px) {
  .navbar-burger {
    display: block;
    margin-left: 10px;
  }

  .navbar-menu {
    display: none;
  }

  .navbar-menu.is-active {
    display: block;
  }
}

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}

.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #3c3c3c;
  border-color: #3c3c3c transparent #3c3c3c transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}

.navbar-burger span {
  background-color: black !important;
  border: none;
}

.navbar-center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}

.navbar-center .navbar-item strong {
  color: black !important;
  font-size: 1.5rem;
}

.navbar-brand .navbar-item,
.navbar-end .navbar-item {
  position: relative;
  color: black !important;
}

.navbar-brand .navbar-item::after,
.navbar-end .navbar-item::after {
  content: "";
  position: absolute;
  bottom: 0px;
  left: 0;
  width: 0;
  height: 2px;
  background-color: black;
  transition: width 0.3s ease-in-out;
}

.navbar-brand .navbar-item:hover::after,
.navbar-end .navbar-item:hover::after {
  width: 100%;
}

.navbar-item form {
  position: relative;
}

.search-container {
  display: flex;
  align-items: center;
  justify-content: center;
}

.search-button {
  background-color: white !important;
  color: #333 !important;
  border: 1px solid #ddd;
}

.search-input {
  background-color: white !important; 
  border: 1px solid #ddd;
  color: black;

  &::placeholder {
    color: #333;
  }
}

.router-link-active {
  background-color: transparent !important;
  color: inherit !important;
  box-shadow: none !important; 
}

.navbar-item:hover {
  background-color: transparent !important; 
}

.navbar {
  border-bottom: black 1px solid;
}

.footer svg {
  width: 24px;
  height: 24px; 
  fill: white !important; 
}

.footer a {
  margin: 0 10px;
}

.section{
  margin: 0;
  padding: 0;
}
</style>