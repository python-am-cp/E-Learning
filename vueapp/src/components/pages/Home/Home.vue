<template>
  <div>
    <h3>E-learning app</h3>
    <ul>
      <li v-if="users != null" v-for="user in users" v-bind:key="user.id">
        {{ user.username }}
      </li>
    </ul>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'home',
  data () {
    return {
      users: []
    }
  },
  mounted () {
    this.getAllUsers()
  },
  computed: {
    ...mapGetters('users', [
      'getUsers'
    ])
  },
  methods: {
    async getAllUsers () {
      await this.$store.dispatch('users/getUsers')
    }
  }
}
</script>
