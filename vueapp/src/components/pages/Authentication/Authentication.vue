<template>
  <div class="l-auth-container">
    <b-navbar class="NB" fixed = top toggleable="sm">
      <b-navbar-brand class="NB-brand" href=""><span style="color:#FFFFFF">E-Learning</span></b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav role="navigation" class="ml-auto">
          <b-nav-item class="nav-item" href="/"><span style="color:#E0FFFF">ELP</span></b-nav-item>
          <b-nav-item class="nav-item" href=""><span style="color:#E0FFFF">О ПРОЕКТЕ</span></b-nav-item>
          <b-nav-item class="nav-item" href="login"><span style="color:#E0FFFF">ВХОД</span></b-nav-item>
          <b-nav-item class="nav-item" href="level"><span style="color:#E0FFFF">НАЧАТЬ ОБУЧЕНИЕ</span></b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <div class="l-auth">
      <v-form v-model="validLogin">
        <v-text-field label="Username"
                      v-model="credentials.username"
                      prepend-icon="account_box"
                      :rules="rules"
                      required
                      color="light-blue lighten-4">
        </v-text-field>

        <v-text-field label="Password"
                      v-model="credentials.password"
                      prepend-icon="lock"
                      :rules="rules"
                      :append-icon="loginPasswordVisible ? 'visibility' : 'visibility_off'"
                      :append-icon-cb="() => (loginPasswordVisible = !loginPasswordVisible)"
                      :type="loginPasswordVisible ? 'text' : 'password'"
                      color="light-blue lighten-4"
                      required>
        </v-text-field>

        <v-btn flat color="light-blue lighten-4" @click.native="signUpVisible = true">Create account</v-btn>
        <v-btn color="light-blue lighten-4" @click.native="submitAuthentication()">Login</v-btn>
      </v-form>
    </div>

    <div class="l-signup" v-if="signUpVisible">
      <v-form v-model="validSignUp">
        <v-text-field label="Username"
                      v-model="newUser.username"
                      prepend-icon="account_box"
                      :rules="rules"
                      required
                      color="light-blue lighten-4">
        </v-text-field>

        <v-text-field label="Password"
                      v-model="newUser.password"
                      prepend-icon="lock"
                      :rules="rules"
                      :append-icon="signUpPasswordVisible ? 'visibility' : 'visibility_off'"
                      :append-icon-cb="() => (signUpPasswordVisible = !signUpPasswordVisible)"
                      :type="signUpPasswordVisible ? 'text' : 'password'"
                      color="light-blue lighten-4"
                      required>
        </v-text-field>

        <v-btn block color="light-blue lighten-4" @click.native="submitSignUp()">Sign Up</v-btn>
      </v-form>
    </div>

    <v-snackbar :timeout="6000"
                bottom="bottom"
                color="red lighten-1"
                v-model="snackbar">
      {{ message }}
    </v-snackbar>
  </div>
</template>
<script>
import Authentication from './index'
export default {
  data () {
    return {
      snackbar: false,
      validLogin: false,
      validSignUp: false,
      signUpVisible: false,
      loginPasswordVisible: false,
      signUpPasswordVisible: false,
      rules: [ (value) => !!value || 'This field is required' ],
      credentials: {
        username: '',
        password: ''
      },
      newUser: {
        username: '',
        password: ''
      },
      message: ''
    }
  },
  methods: {
    submitAuthentication () {
      Authentication.authenticate(this, this.credentials, '/level')
    },

    submitSignUp () {
      Authentication.signup(this, this.newUser, '/level')
    }
  }
}
</script>
<style lang="scss">
  @import "./../../../assets/styles";
  .NB {
    background-color: #09151A;
    height: 9%;
    //position: fixed = top;
  }
  .NB-brand{
    color: #FFFFFF;
    margin: 0 0 0 20px;
  }
  .l-auth {
    background-color: $background-color;
    padding: 15px;
    margin: 100px auto;
    min-width: 272px;
    max-width: 320px;
    animation: bounceIn 1s forwards ease;
  }
  .l-signup {
    background-color: $background-color;
    padding: 15px;
    margin: 45px auto;
    min-width: 272px;
    max-width: 320px;
    animation: slideInFromLeft 1s forwards ease;
  }
</style>
