<template>
    <header class="header">
        <ul> 
            <li> <router-link to="/login">Login |</router-link></li>
            <li> <router-link to="/register">Register</router-link> </li>
        </ul>
        <h1>TodoList</h1>
        <div id="nav">
            <router-link to="/"><p>Retour TodoLists</p></router-link> 
        </div>
    </header>
</template>

<script>
export default {
    name:"Header",

}
</script>

<style scoped>
 .header{
     background: #333;
     color: #fff;
     text-align: center;
     padding: 10px;
 }

 .header a {
     color: #fff;
     padding-right: 5px;
 }

 li {
     display: inline
 }
</style>