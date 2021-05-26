<template>
    <div>
        <h2> Login</h2>
     <div class="container">
         <p> {{ message }}</p>
        <form  @submit.prevent="handleSubmit">

                <label for='usrname'>Username</label>
                <input type='text' name='usrname' id='usrname' v-model='usrname'>
            
                <label for='pwd'>Username</label>
                <input type='password' name='pwd' id='pwd'  v-model='pwd'>
            
                <button type='submit' class='btn waves-effect waves-light lighten-2'>Login</button>
           

        </form>
     </div>
    </div>

</template>

<script>
import axios from 'axios'
export default {
    name: 'Login',
    data() {
        return {
            usrname:'',
            pwd:'',
            message:''
        }
    },
    methods: {
        async handleSubmit() {
            const response = await axios.post(`http://${process.env.VUE_APP_API_HOST}:${process.env.VUE_APP_API_PORT}/api/login`,  {
                usrname: this.usrname,
                pwd: this.pwd
            });
            if (response.data.token) {
                localStorage.setItem('token',response.data.token)
                this.$router.push('/')
            } else {
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