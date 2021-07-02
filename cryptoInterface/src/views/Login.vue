<template>
<v-row class="pt-10" justify="space-around"> 
  <v-col cols="12" sm="4" align-self="end"> 
        <v-form ref="form" method="login">
        <v-text-field
          color="blue"
          outlined
          label="Username"
          type='username'
          @keydown.enter="postLogin"
          prepend-inner-icon="mdi-account"
          v-model="id"
          required            
          ></v-text-field>
        <v-text-field
          color="blue"
          outlined
          prepend-inner-icon="mdi-lock"
          label="Password"
          type='password'
          @keydown.enter="postLogin"
          v-model="password"
          required            
          ></v-text-field>
        <v-btn 
          depressed 
          block
          x-large
          @keydown.enter="postLogin"
          @click="postLogin"
          color="#26B99A" 
          class="white--text" 
          >Login</v-btn>
        </v-form>
    <v-divider class="my-5"></v-divider>

        <div style="text-align:center">
      <v-tooltip bottom>
        <template v-slot:activator="{ on: tooltip }">
          <v-btn text v-on="{ ...tooltip}" class="mr-5" style="background-color:lightgray" @click="dialogPW = true">
            <v-icon>mdi-lock-reset</v-icon>
          </v-btn >
        </template>
        <span>Reset Password</span>
      </v-tooltip>
      <v-tooltip bottom>
        <template v-slot:activator="{ on: tooltip }">
          <v-btn text v-on="{ ...tooltip}" style="background-color:lightgray" @click="dialogPedido = true">
            <v-icon>mdi-text-box-check</v-icon>
          </v-btn >
        </template>
        <span>Registo</span>
      </v-tooltip>
    </div>
    <v-dialog
      v-model="dialogPedido"
      scrollable 
      width="700"
      persistent
    >
      <v-card height="100%" width="100%">
        <v-toolbar color="#2A3F54" dark>
          <h1>Registo de Utilizador</h1>
        </v-toolbar>
        <v-card-actions>
          <v-row
            class="fill-height"
            align="center"
            justify="center"
          >
            <div style="width:500px">
              <v-form ref="form" method="post" enctype="multipart/form-data">
                  <v-container>
                  <v-container/>
                      <v-row>
                        <v-text-field
                            label= "Username"
                            v-model="username"
                            :rules="[rules.required]"
                            required                      
                        ></v-text-field>
                        <h5 style="color:red">*</h5>
                      </v-row>
                      <v-row>
                        <v-text-field
                        label="Password"
                        type='password'
                        v-model="pw"
                        :rules="[rules.required]"            
                        ></v-text-field>
                        <h5 style="color:red">*</h5>
                      </v-row>
                      <v-row>
                        <v-text-field
                            label="Nome"
                            v-model="nome"
                            :rules="[rules.required]"                    
                        ></v-text-field>
                        <h5 style="color:red">*</h5>
                      </v-row>
                      <v-row>
                        <v-text-field
                            label="Email"
                            v-model="email"
                            :rules="[rules.required, rules.email]"
                            required                     
                        ></v-text-field>
                        <h5 style="color:red">*</h5>
                      </v-row>
                      <br>
                      <v-tooltip bottom>
                        <template v-slot:activator="{ on: tooltip }">
                          <v-btn class="mr-5 mb-10 mt-10" @click="post();" v-on="{ ...tooltip}" :disabled="disableButton">
                            <v-icon>mdi-check</v-icon>
                          </v-btn>
                        </template>
                        <span>
                          Registar
                        </span>
                      </v-tooltip>
                      <v-tooltip bottom>
                        <template v-slot:activator="{ on: tooltip }">
                          <v-btn class="mr-5 mb-10 mt-10" @click.prevent="reset" v-on="{...tooltip}">
                            <v-icon>mdi-history</v-icon>
                          </v-btn>
                        </template>
                        <span>
                          Limpar
                        </span>
                      </v-tooltip>
                      
                      <v-tooltip bottom>
                        <template v-slot:activator="{ on: tooltip }">
                          <v-btn class="mb-10 mt-10" @click="dialogPedido = false" v-on="{ ...tooltip}">
                            <v-icon>mdi-exit-to-app</v-icon>
                          </v-btn>
                        </template>
                        <span>
                          Sair
                        </span>
                      </v-tooltip>
                  </v-container>
              </v-form>
            </div>
          </v-row>
        </v-card-actions>
      </v-card>
    </v-dialog>
      </v-col>
  </v-row>
</template>
<script>
/* eslint-disable */
import axios from 'axios'

export default {  
  data(){
    return {
      id: "",
      password: "",
      dialog:false,
      dialogPW:false,
      dialogPedido:false,
      username:"",
      nome:"",
      pw:"",
      email:"",
      favs:[],
      valid:true,
      failureDialog:false,
      rules: {
          required: value => !!value || 'Required.',
          email: value => {
            const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            if(pattern.test(value)){
              this.valid = true
            }else{
              this.valid = false
            }
            return pattern.test(value) || 'Invalid e-mail.'
          },
      },

    }
    },
  created(){
    this.username=''
    this.nome=''
    this.pw=''
    this.email=''
    this.favs=[]
  },
  methods: {
    postLogin: function () {
      console.log("ENTREI NO LOGIN")
      let formtest = {
        "username": this.id,
        "password": this.password
      }
      console.log("FORM:::",formtest)
      axios.post(`http://localhost:5102/users/login`,formtest,{
          headers: {
          }
        }).then((data) => {
          console.log("ESTOU AQUI!!!!!")
          // this.$store.commit("guardaTokenUtilizador", data.data.token)
          //   this.$store.commit("guardaNomeUtilizador", data.data.user)
            this.$router.push( {path:`/`})
          if (data.data.error){
            this.$refs.form.reset()
            this.dialog = !this.dialog
          }
          else if(data.data.users && (data.data.token!=undefined)){
            this.$store.commit("guardaTokenUtilizador", data.data.token)
            this.$store.commit("guardaNomeUtilizador", data.data.user)
            this.$router.push( {path:`/`})
          }
        })
        .catch((e) => console.log(e));
      
      console.log("ESTOU AQUI!!!!!2")
    },
    post: function() {
          let formTest = {
            'username': this.username,
            'name': this.nome,
            'password': this.pw,
            'email': this.email
          }
        console.log("REGISTAR::::",formTest)
        axios.post(`http://localhost:5102/users/signup`,formTest,{
          headers: {
          }
        }).then(data => {
          console.log("DATAAAAAA:", data)
          if(data.data.message){
              this.failureDialog = true
            }
          else{
            this.dialogPedido = false
            this.$refs.form.reset()
            this.$router.push( {path:`/login`} )
          }
        }).catch(e => {
            console.log(e)
        })
    },
    reset () {
      this.$refs.form.reset()
      this.username=''
      this.nome=''
      this.pw=''
      this.email=''
    }
  },
  computed:{
    disableButton (){
        if(this.username){
            if (this.valid && this.username.length > 0 && this.nome.length > 0 && this.pw.length > 0 && this.email.length > 0)
                return false
            else
                return true
        }
        else{
            return true
        }
    } 
  },
}
</script>
