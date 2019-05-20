<template>
  <v-app style="background-color:#ddd;">
    <div style="margin: 0 auto; width:700px">
      <v-toolbar fixed color="blue-grey darken-2">
        <v-toolbar-title>
          <router-link to="/" tag="span" style="cursor: pointer">
            TODO
          </router-link>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn flat v-on:click="notify">
          <v-icon>notification_important</v-icon>
          <div class="hidden-xs-only">{{ overdue_cnt }}</div>
        </v-btn>
        <v-toolbar-items v-for="item in menuItems" v-bind:key="item.title">
          <v-btn flat :key="item.title" :to="item.route">
            <v-icon left>{{ item.icon }}</v-icon>
            <div class="hidden-xs-only">{{ item.title }}</div>
          </v-btn>
        </v-toolbar-items>
      </v-toolbar> 
      <main style="margin-top:80px;">
        <router-view></router-view>
      </main>
    </div>
    <notifications group="foo" position="bottom right" />
  </v-app>
</template>

<script>
export default {
  name: 'App',

  data () {
    return {
      overdues: [],
      overdue_cnt: 0
    }
  },

  created() {
    this.$store.dispatch('getOverdue').then(res => {
      this.overdues = res
      this.overdue_cnt = this.overdues.length
    }, error => {
      console.log('getOverdue error: ', error)
    })
  },

  computed: {
      menuItems () {
        let items = [
          // { icon: 'face', title: 'Register', route: '/signup' },
          // { icon: 'lock_open', title: 'Login', route: '/signin' },
          { icon: 'create', title: 'Create Todo', route: '/create' }
        ]
        // if (this.userIsAuthenticated) {
        //   items = [
        //     {icon: 'notifications', title: 'Alarm', route: '/alarm'},
        //     {icon: 'chat', title: 'Chat', route: '/chat'},
        //     {icon: 'account_circle', title: 'MyPage', route: '/mypage'}
        //     //{icon: 'chat', title: 'Logout', route: '/'},
        //   ]
        // }
        return items
      },
      userIsAuthenticated () {
        // return "token" in localStorage
        return this.$store.getters.user !== null && this.$store.getters.user !== undefined || "token" in localStorage
      },
      onlineUsers () {
        console.log(this.$store.getters.onlineUsers)
        return this.$store.getters.onlineUsers
      }
  },
  methods: {
    notify () {
      console.log(this.overdue_cnt)
      if (this.overdue_cnt > 0) {
        this.$notify({
            group: 'foo',
            // title: '<h4>Nothing!</h4>',
            title: 'Overdue : ' + this.overdues[this.overdue_cnt - 1].todo_title,
            text: this.overdues[this.overdue_cnt - 1].deadline_str,
            type: 'error',
            duration: -10
        })
        this.overdue_cnt -= 1
      }
    }
  }



}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
