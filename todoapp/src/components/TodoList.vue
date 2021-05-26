<template>
    <div>
        <h1> Todo List </h1>
         <!-- todos fait référence à la props todos ci-dessous -->
         <div class="row">
            <div v-bind:key="todolist.id_list" v-for="todolist in todolists">
                <TodoListItem v-bind:todolist="todolist" v-on:del-todolist="$emit('del-todolist',todolist.id_list)" v-on:update-todolist="$emit('update-todolist',todolist.id_list,todolist.name_list)" />
            </div>
        </div>
    </div>
</template>z

<script>
import TodoListItem from './TodoListItem.vue';


export default {
    name: "TodoList",
    components: {
        TodoListItem,
    
    },
    props: ["todolists"],
    methods: {
       
    }
}
</script>

<style scoped>

    /* Remove extra left and right margins, due to padding in columns */
    .row {margin: 0 -5px;}

    /* Clear floats after the columns */
    .row:after {
        content: "";
        display: table;
        clear: both;
    }

</style>