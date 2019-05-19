import Vue from 'vue'
import Router from 'vue-router'
import Todos from '@/components/Todos'
import CreateTodo from '@/components/CreateTodo'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Todos',
      component: Todos
    },
    {
      path: '/create',
      name: 'CreateTodo',
      component: CreateTodo
    }
  ]
})
