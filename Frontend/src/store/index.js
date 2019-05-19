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
    getTodos ({commit}, payload) {
      return new Promise((resolve, reject) => {
        axios.get(`api/v1/`).then(res => {
          resolve(res.data)
        }).catch((e) => {
          console.log('get todo err: ', e)
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
    }
  },

  getters: {

  }
})
