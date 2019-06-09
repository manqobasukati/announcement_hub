//componets

let HomePageHeader = Vue.component('home-page-header',{
	computed:{
		sizeOfAnnouncements(){
			return store.getters.sizeOfAnnouncements;
		}
	},
	template:`
			<div class="components home-page-header">
				
				<v-container grid-list-md>
					<v-layout row wrap>
						<v-flex xs10>
							<h1>Pending Announcements</h1>
						</v-flex>
						<v-flex xs2>
							<h1>{{sizeOfAnnouncements}}</h1>
						</v-flex>
					</v-layout>
				</v-container>
			</div>`
});

let AnnouncementHome = Vue.component('announcement-home',{
	computed:{
		getAllAnnouncements(){
			return store.getters.getAllAnnouncements;
		},
		sizeOfAnnouncements(){
			console.log("Here");
			return store.getters.sizeOfAnnouncements;
		},
		
		todaysDate(){
			var today = new Date();
			var dd = today.getDate();
			var mm = today.getMonth()+1; //January is 0!
			var yyyy = today.getFullYear();

			if(dd<10) {
				dd = '0'+dd
			} 

			if(mm<10) {
				mm = '0'+mm
			} 

			today = mm + '/' + dd + '/' + yyyy;
			return today;
		}
	},
	methods:{
		
	},
	
	template:`
			<div class="components radio-announcement-home">
				<h2>{{todaysDate}}</h2>
				<v-container grid-list-md>
					<v-layout row wrap>
						<v-flex v-for="i in getAllAnnouncements"  xs4>
						 <v-card dark color="primary">
							 
							 <v-card-title>
							  <div>
								<v-card-text class="px-0">{{i}}</v-card-text>
							  </div>
							</v-card-title>
						</v-card>
					  </v-flex>
					</v-layout>
				</v-container>
			</div>
	`
});


let PrintAnnouncementHome = Vue.component('print-announcement-home',{
	template:`
		<div class="components print-announcement-home">
			
		</div>
	`
})




