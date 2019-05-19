<template>
  <v-app style="background-color:#ddd">
    <v-toolbar color="blue-grey darken-2" style="position:fixed; z-index:10000000">
      <v-toolbar-title>
        <router-link to="/" tag="span" style="cursor: pointer">
          TODO
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items v-for="item in menuItems" v-bind:key="item.title">
        <v-btn flat :key="item.title" :to="item.route">
          <v-icon left>{{ item.icon }}</v-icon>
          <div class="hidden-xs-only">{{ item.title }}</div>
        </v-btn>
      </v-toolbar-items>
    </v-toolbar> 
    <main style="margin-top:100px;">
      <router-view></router-view>
    </main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
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
