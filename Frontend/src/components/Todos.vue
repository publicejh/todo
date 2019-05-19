<template>
  <div v-if="todosReady">
    <v-list two-line>
          <v-flex v-for="(todo, index) in todos" v-bind:key="todo.id">
            <v-list-tile
              avatar
              ripple
              @click=""
            >
              <v-list-tile-content>
                <v-list-tile-title>{{ todo.todo_title }}</v-list-tile-title>
                <v-list-tile-sub-title class="text--primary">{{ todo.modified_time }}</v-list-tile-sub-title>
                <v-list-tile-sub-title>{{ todo.todo_content }}</v-list-tile-sub-title>
              </v-list-tile-content>

              <v-list-tile-action>
                <v-list-tile-action-text>{{ todo.deadline }}</v-list-tile-action-text>
                <v-list-tile-action-text>{{ todo.priority_name }}</v-list-tile-action-text>

                <v-btn small v-if="todo.status == 0">발의</v-btn>
                <v-btn small color="success" v-else-if="todo.status == 1">진행</v-btn>
                <v-btn small color="primary" v-else-if="todo.status == 2">완료</v-btn>
                <v-btn small disabled v-if="todo.is_deleted">삭제</v-btn>
              </v-list-tile-action>

            </v-list-tile>
            <v-divider
              v-if="index + 1 < todos.length"
              :key="index"
            ></v-divider>
          </v-flex>
        </v-list>
  </div>
</template>

<script>
export default {
  name: 'Todos',
  data () {
    return {
      todosReady: false,
      todos: []
    }
  },

  created () {
    this.$store.dispatch('getTodos').then(res => {
      this.todosReady = true
      this.todos = res
    }, error => {
      console.log('getTodos error: ', error)
    })
  },

  mounted () {
  },

  computed: {

  }

}
</script>
