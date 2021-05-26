<template>
    <div>
        <form  @submit="addTodoList">
            <input type="text" v-model="name" name="name" placeholder="  Ajouter une TodoList...">
            <button class="btn waves-effect waves-light lighten-2" type="submit">Ajouter 
                <i class="material-icons right">send</i>
            </button>
        </form>
    </div>
</template>

<script>

export default {
    name: "AddTodoList",
    data() {
        return {
            name:''
        }
    },
    methods: {
        addTodoList(e) {
            e.preventDefault();
            // On construit l'objet newTodo
            const newTodoList = {
                name: this.name,
            }
            // On l'envoie au parent
            this.$emit('add-todolist',newTodoList);

            // Efface dans la barre de saisie une fois ajouté
            this.name = '';
        }
    }
}
</script>

<style scoped>
    
</style>
