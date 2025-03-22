<template>
    <div class="page-log-in">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Log In</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-black">Log In</button>
                        </div>
                    </div>

                    <hr>
                    Don't have an account yet?
                    <router-link to="/sign-up"> Click here</router-link> to sign up!
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = "Log In - Ecommerce"
    },
    methods: {
        async submitForm() {
            axios.defaults.headers.common['Authorization'] = '';

            localStorage.removeItem('token');

            const formData = {
                username: this.username,
                password: this.password
            }

            axios
                .post('/api/v1/token/login/', formData) // Send request from the server
                .then(response => {
                    const token = response.data.auth_token // Get response as token

                    this.$store.commit('setToken', token) // Call the store to set the token with information from the server

                    axios.defaults.headers.common['Authorization'] = `Token ${token}` // Set default header to token

                    localStorage.setItem('token', token) // Store the token in the local storage

                    const toPath = this.$route.query.to || '/cart' // If in page 'cart', go to login page, and goes back that after login

                    this.$router.push(toPath)
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }

                        console.log(JSON.stringify(error.response.data))
                    } else {
                        this.errors.push('An error occurred. Please try again later.')

                        console.log(JSON.stringify(error))
                    }
                })
        }
    }
}
</script>

<style scoped>
.page-log-in {
    color: black;
    height: 500px;
    margin-top: 50px;
}

.title {
    color: black;
}

.input {
    background-color: white;
    color: black; 
    border: 1px solid #ddd; 
}

.button.is-black {
    color: white;
    background-color: black; 
}

label {
    font-weight: bold;
    color: black;
}

a {
    color: black;
    text-decoration: underline;
}

.notification.is-danger {
    color: black;
    background-color: #f8d7da;
    border: 1px solid #f5c6cb;
}
</style>