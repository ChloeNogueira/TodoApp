<template>
    <div>
        <br>
        <AddTodo v-on:add-todo="addTodo"/>
        <br>
        <Todos v-bind:todos="todos" v-on:del-todo="deleteTodo" v-on:update-todo="updateTodo"/>
    </div>
</template>
<script>
import axios from 'axios';
import Todos from '../components/Todos';
import AddTodo from '../components/AddTodo';

export default {
    components:{
        Todos,
        AddTodo
    },
    props: [
        'id',
    ],
    data() {
        return {
            todos: [

            ]
        }
    },
    methods: {
        async deleteTodo(id_list,id) {
            axios.delete(`http://${process.env.VUE_APP_API_HOST}:${process.env.VUE_APP_API_PORT}/api/lists/todos/${id_list}/${id}`)
            .then(res => this.todos = res.data['data'].filter(todo => todo.id_list == id_list))
            .catch(err => console.log(err));
        },
        async updateTodo(id_list,id,name,created_on) {
            axios.patch(`http://${process.env.VUE_APP_API_HOST}:${process.env.VUE_APP_API_PORT}/api/lists/todos/${id_list}/${id}`, {
            name,created_on
            })
            .then(res => this.todos[id] = res.data['data'])
            .catch(err => console.log(err));
        },
        addTodo(newTodo) {
            const {name} = newTodo
            const { created_on } = newTodo
            axios.put(`http://${process.env.VUE_APP_API_HOST}:${process.env.VUE_APP_API_PORT}/api/lists/todos/${this.id}/1`, {
            name, created_on
        })
            .then(res =>  this.todos.push(res.data['data']))
            .catch(err => console.log(err));
        }
       
    },
    async created() {
        axios.get(`http://${process.env.VUE_APP_API_HOST}:${process.env.VUE_APP_API_PORT}/api/lists/todos/${this.id}`)
        .then(res => this.todos = res.data['data']) //this.todos = res.data
        .catch(err => console.log(err));
    }
}
</script>