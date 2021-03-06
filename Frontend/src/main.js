// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import { store } from './store'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import datePicker from 'vue-bootstrap-datetimepicker'
import 'bootstrap/dist/css/bootstrap.css'
import 'pc-bootstrap4-datetimepicker/build/css/bootstrap-datetimepicker.css'
import VueCookie from 'vue-cookie'
import Notifications from 'vue-notification'
import moment from 'moment'
import VueMomentJs from 'vue-momentjs'


Vue.use(datePicker)
Vue.use(Vuetify, {
  iconfont: 'md'
})
Vue.use(VueCookie)
Vue.use(Notifications)
Vue.use(VueMomentJs, moment)
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
