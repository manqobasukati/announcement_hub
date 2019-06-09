const store = new Vuex.Store({
			state:{
				http_name_space:'http://127.0.0.1:5000',
				media_house:{},
				announcements:[]
			},
			mutations:{
				GET_LOGGED_IN_USER(state, payload){
					//state.media_house = 
					//const axios = require('axios');

					// Make a request for a user with a given ID
					axios.get(state.http_name_space+'/dashboard/logged-in-user')
					  .then(function (response) {
						// handle success
						state.media_house = response.data.media_house;
						console.log(response.data.media_house.media_id);
					  })
					  .catch(function (error) {
						// handle error
						console.log(error);
					  })
					  .then(function () {
						// always executed
						console.log(state)
					  });
					  
				},
				GET_ALL_ANNOUNCEMENTS(state, payload){
					axios.get(state.http_name_space+'/dashboard/all-announcements')
					  .then(function (response) {
						// handle success
						state.announcements = response.data.announcements;
						console.log(response.data.announcements);
					  })
					  .catch(function (error) {
						// handle error
						console.log(error);
					  })
					  .then(function () {
						// always executed
						console.log(state)
					  });
				}
			},
			actions:{
				GET_LOGGED_IN_USER_ACTION(state,payload){
					state.commit('GET_LOGGED_IN_USER');
				},
				GET_ALL_ANNOUNCEMENTS_ACTION(state, payload){
					state.commit('GET_ALL_ANNOUNCEMENTS');
				}
				
			},
			getters:{
				sizeOfAnnouncements(state){
					return state.announcements.length;
				
			},
			
				getAllAnnouncements(state){
					ann = []
					//Thu, 14 Feb 2019 10:08:00 GMT
					//js "Sun Feb 24 2019"
					today = new Date();
					dt = today.toDateString();
					//str = "Thu, 14 Feb 2019 10:08:00 GMT";
					//day = str.substr(5,2);
					//month = str.substr(8,3);
					//year = str.substring(13,4);
					//console.log(state.announcements[0]['from_date']);
					
			
					for(var i= 0;i<=state.announcements.length -1;i++)
					{
						//console.log(state.announcements[i]['from_date']);
						if(state.announcements[i]['from_date'].substr(5,2) == dt.substr(8,2) 
								&& 
							state.announcements[i]['from_date'].substr(8,3) == dt.substr(4,3)
								&&
							state.announcements[i]['from_date'].substr(12,4) == dt.substr(11,4))
							{
								ann[i] = state.announcements[i];
							}
					}
					console.log(ann);
					
					
					
					return ann;
				}
			}
});