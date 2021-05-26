<template>
    <div>
        <h2> Register </h2>
     <div class="container">
         <p> {{ message }} </p>
        <form @submit.prevent="handleSubmitAuth">

                <label for='usrnameauth'>Username</label>
                <input type='text' name='usrnameauth' id='usrnameauth' v-model='usrnameauth'>
            
                <label for='pwdauth'>Username</label>
                <input type='password' name='pwdauth' id='pwdauth'  v-model='pwdauth'>
            
                <button type='submit' class='btn waves-effect waves-light lighten-2'>Login</button>
           

        </form>
     </div>
    </div>

</template>

<script>
import axios from "axios"

export default {
    name: 'Register',
    data() {
        return {
            message:'' ,
            usrnameauth:'',
            pwdauth:'',
        }
    },
  
    methods: {
        async handleSubmitAuth() {
            const response = await axios.post(`http://${process.env.VUE_APP_API_HOST}:${process.env.VUE_APP_API_PORT}/api/account`,  {
                usrnameauth: this.usrnameauth,
                pwdauth: this.pwdauth
            });
            if(response.data.status == '201') {
                this.$router.push('/login')
            }else {
                this.message = response.data.message
            }        
        }
    }
    
}
</script>

<style scoped>
    .container {
        padding: 2px 16px;
        width: 30%;
    }
    input {
        width: 10%;
    }
</style>