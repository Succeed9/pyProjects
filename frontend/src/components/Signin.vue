<template>
  <div class="signin">
    <h1>Вход</h1>
    <form @submit.prevent="signin">
      <input type="text" v-model="username" placeholder="Username" required />
      <input type="password" v-model="password" placeholder="Password" required />
      <button type="submit">Войти</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    async signin() {
      try {
        const response = await axios.post('http://localhost:5000/signin', {
          username: this.username,
          password: this.password
        });
        localStorage.setItem('token', response.data.access_token);
        this.$router.push('/');
      } catch (error) {
        console.error('Error during sign in:', error);
      }
    }
  }
};
</script>