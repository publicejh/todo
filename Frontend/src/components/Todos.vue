<template>
  <div v-if="todosReady">
    <v-card flat style="margin-bottom: 10px">
    <v-card-text>
      <v-container fluid>
        <v-layout row wrap>
          <v-flex xs3 sm3 md3>
            <v-checkbox
              v-model="filterByPriority"
              label="중요"
              color="red"
              value="important"
              hide-details
            ></v-checkbox>
            <v-checkbox
              v-model="filterByStatus"
              label="발의"
              color="grey"
              value="todo"
              hide-details
            ></v-checkbox>
          </v-flex>
          <v-flex xs3 sm3 md3>
            <v-checkbox
              v-model="filterByPriority"
              label="보통"
              color="darkkhaki"
              value="normal"
              hide-details
            ></v-checkbox>
            <v-checkbox
              v-model="filterByStatus"
              label="진행"
              color="green"
              value="doing"
              hide-details
            ></v-checkbox>
          </v-flex>
          <v-flex xs3 sm3 md3>
            <v-checkbox
              v-model="filterByPriority"
              label="사소"
              color="grey"
              value="trivial"
              hide-details
            ></v-checkbox>
            <v-checkbox
              v-model="filterByStatus"
              label="완료"
              color="blue"
              value="done"
              hide-details
            ></v-checkbox>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card-text>
  </v-card>
  
    <v-list two-line>
          <v-flex v-if="filter(todo)" v-for="(todo, index) in todos" v-bind:key="todo.id">
            <v-list-tile
              avatar
              ripple
              v-on:click="jumpToDetail(todo.id)"
            >
              <v-list-tile-content>
                <v-list-tile-title>{{ todo.todo_title }}</v-list-tile-title>
                <v-list-tile-sub-title>{{ todo.todo_content }}</v-list-tile-sub-title>
              </v-list-tile-content>

              <v-list-tile-action>
                <v-list-tile-action-text>{{ todo.deadline_str }}</v-list-tile-action-text>
                <v-list-tile-action-text :class="priority_class(todo.priority)">{{ todo.priority_name }}</v-list-tile-action-text>

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
      todos: [],
    //   ex4: ['important', 'normal', 'trivial', 'todo', 'doing', 'done'],
      filterByPriority: ['important', 'normal', 'trivial'],
      filterByStatus: ['todo', 'doing', 'done'],

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
  },

  methods: {
    jumpToDetail (todo_id) {
      this.$router.push("/" + todo_id)
    },

    priority_class(priority) {
    var classType = ''

    switch ( priority ) {
        case 0:
            classType = 'important'
            break
        case 1:
            classType = 'normal'
            break
        case 2:
            classType = 'trivial'
            break
        default:
            classType = ''
    }

      return classType
    },

    filter (todo) {
        var priorities = ['important', 'normal', 'trivial']
        var statuses = ['todo', 'doing', 'done']

        if (this.filterByPriority.includes(priorities[todo.priority]) && this.filterByStatus.includes(statuses[todo.status])) {
            return true
        } else {
            return false
        }
    },

    overdue_class (todo) {
        return (todo.is_overdue ? 'overdue' : '')
    }
  },

}
</script>
<style>
  .important{
      color:red;
  }
  .normal{
      color:darkkhaki;
  }
  .trivial{
      color:grey;
  }
  .overdue{
      background-color:#F0E0E0;
  }
</style>