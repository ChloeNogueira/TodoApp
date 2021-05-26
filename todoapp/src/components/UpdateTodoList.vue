<template>
    <form @submit="updateTodoList">
        <div >
            <input v-model="name" class="inputSize" type="text" name="newtitle" placeholder="New title here..."/>
        </div>
        <button type="submit" class="btn waves-effect waves-light lighten-2">Save Update
                <i class="material-icons right">send</i>
        </button>
    </form>
</template>

<script>
export default {
    name: 'UpdateTodoList',
    data () {
        return {
            name: ''
        }
    },
    methods: {
        updateTodoList(e) {
            e.preventDefautl();
            // On construit l'objet newTitleTodoList
            const newTitleTodoList = {
                name: this.name,
            }
            // On l'envoie au parent
            this.$emit('update-todolist',newTitleTodoList);
            // Efface dans la barre de saisie une fois ajouté
            this.name = '';
        }
    }
}
</script>
<style scoped>
.inputSize {
    width:20%
}
</style>