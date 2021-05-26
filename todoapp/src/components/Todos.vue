<template>
    <div>
        <h1> Todos </h1>
         <!-- todos fait référence à la props todos ci-dessous -->
        <div class="row">
            <div v-bind:key="todo.id_list+'/'+todo.id" v-for="todo in todos">
                <Todo v-bind:todo="todo" v-on:del-todo="$emit('del-todo',todo.id_list,todo.id)" v-on:update-todo="$emit('update-todo',todo.id_list,todo.id,todo.task['name'],todo.task['created_on'])"/>
            </div>
        </div>
    </div>
    
</template>
<script>
import Todo from './Todo'

export default {
    name:'Todos',
    props:['todos'],
    components: {
        Todo,
    }
    
}
</script>