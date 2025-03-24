<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Sign up</h1>

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

                    <div class="field">
                        <label>Repeat password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password2">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-black">Sign up</button>
                        </div>
                    </div>

                    <hr>

                    Or <router-link to="/log-in">click here</router-link> to log in!
                </form>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios';
import {toast} from 'bulma-toast';
export default {
    name: 'SignUp',
    data() {
        return {
            username: '',
            password: '',
            password2: '',
            errors: []  
        }
    },
    mounted() {
        document.title = 'Sign Up - URBANFIT'
    },  
    methods: {
        submitForm() {
            this.errors = []

            if (this.username === '') {
                this.errors.push('The username field is required.')
            }
            if (this.password === '') {
                this.errors.push('The password field is too short.')
            }
            if (this.password !== this.password2) {
                this.errors.push('The passwords do not match.')
            }

            if (!this.errors.length){
                const formData = {
                    username: this.username,
                    password: this.password
                }

                axios
                    .post('/api/v1/users/', formData)
                    .then(response => {
                        toast({
                            message: 'User created successfully!',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right'
                        })
                        this.$router.push('/log-in')
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
}
</script>

<style scoped>
.page-sign-up {
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