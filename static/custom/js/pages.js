
let LayoutPage = Vue.component('layout-page',{
	data(){
		return{
			title:'Welcome home'
		}
	},
	template:`
		<div class="pages layout-page">
			<v-app>
				<nav-bar/>
				<router-view></router-view>
				<footer-bar></footer-bar>
			</v-app>
		</div>
		`
})

let HomePage = Vue.component('home-page',{
	data(){
		return{
			title:'Welcome home'
		}
	},
	template:`
		<div class="pages home">
			<v-container grid-list-md >
				<v-layout row wrap>
					<v-flex xs12>
						<home-page-header></home-page-header>
						 <v-divider ></v-divider>
						 <announcement-home></announcement-home>
					</v-flex>
				</v-layout>
			</v-container>
		</div>
	`
});


let SetRatesPage = Vue.component('set-rates-page',{
	data(){
		return{
			title:'Set your rates here'
		}
	},
	template:`
		<div class="pages home">
			<v-container grid-list-md >
				<v-layout row wrap>
					<v-flex xs12>
						<h1>{{title}}</h1>
					</v-flex>
				</v-layout>
			</v-container>
		</div>
	`
});


let ProfilePage = Vue.component('profile-page',{
	data(){
		return{
			title:'Change profile here'
		}
	},
	template:`
		<div class="pages home">
			<v-container grid-list-md >
				<v-layout row wrap>
					<v-flex xs12>
						<h1>{{title}}</h1>
					</v-flex>
				</v-layout>
			</v-container>
		</div>
	`
})
