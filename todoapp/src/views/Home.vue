<template>
  <div class="home">
    <AddTodoList v-on:add-todolist="addTodoList" />
    <TodoList v-bind:todolists="todolists" v-on:del-todolist="deleteTodoList" v-on:update-todolist="updateTodoList"  />
  </div>
</template>

<script>
import TodoList from '../components/TodoList';
import AddTodoList from '../components/AddTodoList';

import axios from 'axios';

export default {
  name: 'Home',
  components: {
    TodoList,
    AddTodoList,
  },
  data() {
    return{
      todolists: [
        
      ]
    }
  },
  methods: {
    async deleteTodoList(id_list) {
      axios.delete(`http://${process.env.VUE_APP_API_HOST}:${process.env.VUE_APP_API_PORT}/api/lists/${+id_list}`)
      .then(res => this.todolists = res.data['data'])
      .catch(err => console.log(err));
      
    },
    addTodoList(newTodoList) {
      const { name } = newTodoList;

      axios.put(`http://${process.env.VUE_APP_API_HOST}:${process.env.VUE_APP_API_PORT}/api/lists/1`, {
        name
      })
      .then(res =>  this.todolists.push(res.data['data']))
      .catch(err => console.log(err));
    },
    async updateTodoList(id_list,name_list) {
            axios.patch(`http://${process.env.VUE_APP_API_HOST}:${process.env.VUE_APP_API_PORT}/api/lists/${id_list}`, {
            name_list
            })
            .then(res => this.todolists[id_list] = res.data['data'])
            .catch(err => console.log(err));
    }
  },
  async created() {
    axios.get(`http://${process.env.VUE_APP_API_HOST}:${process.env.VUE_APP_API_PORT}/api/lists`)
    .then(res => this.todolists = res.data['data']) //this.todos = res.data
    .catch(err => console.log(err));
  }
}
</script>
<style >



body{
  font-family: Arial, Helvetica, sans-serif;
  line-height: 1.4;
}
</style>