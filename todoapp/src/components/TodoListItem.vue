<template>
    <div class="column">
        <div class="todo-item  card"> 
            <div class="container">
                <div class="topright"> 
                    <button @click="$emit('del-todolist',todolist.id_list)" class="btn-floating btn-small waves-effect waves-light red"><i class="material-icons">cancel</i>
                    </button>
                </div>
                <p> {{ required }} </p>
                <h4 v-if="!editing" @dblclick="edit()"> TodoList:{{todolist.name_list}} </h4>
                <input v-else type="text" v-model="todolist.name_list" @blur="doneEdit()" @keyup.enter="doneEdit()">
                <router-link :to="{name:'Todos', params: {id:todolist.id_list}}" style="color:black">
                    <button type="button" class="btn waves-effect waves-light lighten-2">Voir la liste <i class="material-icons right">send</i></button>
                </router-link>
            </div>
        </div>
    </div>
</template>
<script>


export default {
    name: "TodoListItem",
    props: ["todolist"],
    components: {
     
    },
    data () {
        return {
            name: '',
            editing:false,
            required:''
        }
    },
    methods: {
      edit() {
          this.editing = true
      },
      doneEdit() {

        if(this.todolist.name_list != ""){
          this.required = ""
          this.editing = false
          this.$emit('update-todolist',this.todolist.id_list,this.todolist.name_list)
        }else {
            this.required = "Vous devez saisir un titre"
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
    /* Float four columns side by side */
    .column {
        float: left;
        width: auto;
        padding: 0 10px;
    }


    .topright {
        position: absolute;
        top: 8px;
        right: 16px;
        font-size: 18px;
    }

    

  
</style>