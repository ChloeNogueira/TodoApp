<template>
    <div>
        <form  @submit="addTodo">
            <input type="text" v-model="name" name="name" placeholder="Titre du Todo...">
            <input type="date" v-model="created_on" name="created_on" placeholder="Date de création...">
            <button class="btn waves-effect waves-light lighten-2" type="submit">Ajouter Todo
                <i class="material-icons right">send</i>
            </button>
        </form>
    </div>
</template>

<script>

export default {
    name: "AddTodo",
    data() {
        return {
            name:'',
            created_on:''
        }
    },
    methods: {
        addTodo(e) {
            e.preventDefault();
            const newTodo = {
                name: this.name,
                created_on:  this.created_on
            }
            // On l'envoie au parent
            this.$emit('add-todo',newTodo);

            // Efface dans la barre de saisie une fois ajouté
            this.name = '';
            this.created_on = '';
        }
    }
}
</script>

<style scoped>
    
</style>
