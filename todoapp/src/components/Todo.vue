<template>
   <div class="todo-item " > 
        <div class="container">
            <p> {{ required }} </p>
            <p v-if="!editing" @dblclick="edit()"> {{todo.task['name']}} </p>
            <input v-else type="text" v-model="todo.task['name']" @blur="doneEdit()" @keyup.enter="doneEdit()">

            <p> Created on: </p><p v-if="!editing" @dblclick="edit()"> {{todo.task['created_on']}} </p>
            <input v-else type="date" v-model="todo.task['created_on']" @blur="doneEdit()" @keyup.enter="doneEdit()">
          
             <button @click="$emit('del-todo',todo.id_list,todo.id)" class=" btn-floating btn-small waves-effect waves-light red"><i class="material-icons">cancel</i>
            </button> 
            
        </div>
    </div>
</template>
<script>

export default {
    name: 'Todo',
    props: ['todo'], 
    data () {
        return {
            editing:false,
            required:""
        }
    },
    methods: {
        edit() {
            this.editing = true
        },
        doneEdit() {
          if((this.todo.task['created_on'] != "") && (this.todo.task['name'] != "")){
                this.required = ""
                this.editing = false
                this.$emit('update-todo',this.todo.id_list,this.todo.id,this.todo.task['name'],this.todo.task['created_on'])
          }else {
                this.required = "Vous devez saisir tous les champs"
                //if(this.todo.task['created_on'] == ""){
                //    this.todo.task['created_on'] = "Attention vous n'avez pas saisi de date !"
                //}
                //if(this.todo.task['name'] == ""){
                //    this.todo.task['name'] = "Attention vous n'avez pas saisi de nom !"
                //}   
          }
        }
    }
    
}
</script>

<style scoped>
    .todo-item {
        background: #f4f4f4;
        padding: 10px;
        border-bottom: 1px #ccc dotted;
        width: 30%;
        margin:auto;
    }

    .card {
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        width: auto;
    }

    .card:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }

    .container {
        padding: 2px 16px;
        width: auto;
    }
</style>