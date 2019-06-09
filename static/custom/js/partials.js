//partials page

let NavBar = Vue.component('nav-bar',{
	computed:{
		title(){
			return store.state.media_house.media_house_name;
		},
		http_name_space(){
			return store.state.http_name_space;
		}
	
	},
	template:`
		<div class="partials nav-bar purple darken-2 text-xs-center">
			
			<v-toolbar class="purple darken-2 text-xs-center white--text">
				<img src="http://127.0.0.1:5000/static/images/ahub_logo/logo_3.png" width="50"/>
				<v-toolbar-title>{{title}}</v-toolbar-title>
				<v-spacer></v-spacer>
				<v-toolbar-items class="hidden-sm-and-down">
				  <v-btn flat ><router-link to="/home" class="white--text">Announcements</router-link></v-btn>
				  <v-btn flat class="white--text"><router-link to="/set-rates" class="white--text">Set rates</router-link></v-btn>
				  <v-btn flat class="white--text"><router-link to="/profile" class="white--text">Profile</router-link></v-btn>
				</v-toolbar-items>
			</v-toolbar>
		</div>
	`
})

let FooterBar = Vue.component('footer-bar',{
	template:`
		<div class="partials footer-bar">
			<v-footer class="pa-3 purple darken-2">
				<v-spacer></v-spacer>
				<div>&copy; {{ new Date().getFullYear() }}</div>
			</v-footer>
		</div>`
});