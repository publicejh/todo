import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
  },

  mutations: {
  },

  actions: {
    getTodo ({commit}, payload) {
      return new Promise((resolve, reject) => {
        axios.get(`api/v1/${payload}/`).then(res => {
          resolve(res.data)
        }).catch((e) => {
          console.log('get todo err: ', e)
          reject(e)
        })
      })
    },
    getTodos ({commit}, payload) {
      return new Promise((resolve, reject) => {
        axios.get(`api/v1/`).then(res => {
          resolve(res.data)
        }).catch((e) => {
          console.log('get todos err: ', e)
          reject(e)
        })
      })
    },
    createTodo ({commit}, payload) {
      return new Promise((resolve, reject) => {
        axios.post(`api/v1/create/`, {
          todo_title: payload.title,
          todo_content: payload.content,
          priority: payload.priority,
          deadline: payload.deadline
          },
          {
            headers: {'X-CSRFToken': payload.csrfToken}
          }
        ).then(res => {
          resolve(res)
        }).catch((e) => {
          console.log('create todo err: ', e)
          reject(e)
        })
      })
    },
    updateTodo ({commit}, payload) {
      return new Promise((resolve, reject) => {
        axios.put(`api/v1/${payload.id}/`, {
          todo_title: payload.title,
          todo_content: payload.content,
          priority: payload.priority,
          status: payload.status,
          deadline: payload.deadline
          },
          {
            headers: {'X-CSRFToken': payload.csrfToken}
          }
        ).then(res => {
          resolve(res)
        }).catch((e) => {
          console.log('update todo err: ', e)
          reject(e)
        })
      })
    },
    deleteTodo ({commit}, payload) {
      return new Promise((resolve, reject) => {
        axios.delete(`api/v1/${payload.id}/`, {
            headers: {'X-CSRFToken': payload.csrfToken}
          }
        ).then(res => {
          resolve(res)
        }).catch((e) => {
          console.log('delete todo err: ', e)
          reject(e)
        })
      })
    },
    getOverdue ({commit}, payload) {
      return new Promise((resolve, reject) => {
        axios.get(`api/v1/overdue/`).then(res => {
          resolve(res.data)
        }).catch((e) => {
          console.log('get overdue err: ', e)
          reject(e)
        })
      })
    }
  },

  getters: {

  }
})
