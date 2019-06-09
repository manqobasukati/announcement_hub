from flask import render_template, redirect, url_for, request,jsonify
from flask_login import login_required, current_user
from app import db
from models import Media, Announcement
from dashboard import dashboard_print


@dashboard_print.route("/logged-in-user", methods=['GET','POST'])
def dashboard_logged_in_user_view_api():
	media_house = Media.query.filter_by(id=current_user.id).first()
	media = {'media_house_name':media_house.media_name,'media_id':media_house.id, 'media_type':media_house.media_type}
	return jsonify({'media_house':media})
	
	
@dashboard_print.route('/all-announcements',methods=['GET','POST'])
def dashboard_all_announcements():
	announcements = Announcement.query.filter_by(media_id = current_user.id).first()
	p = []
	i = 0
	#print(data['user_id'])
	for announcement in Announcement.query.filter_by(media_id=current_user.id).all():
		k = {}
		k['from_date'] = announcement.start_day
		k['to_date'] = announcement.end_day
		k['id'] = announcement.id
		k['read'] = announcement.announced
		#print(announcement.radio_media_announcement[0].radio_media_announcement_time_slot[0].time_slot)
		#if announcement.radio_media_announcement:
			#k['time_slot'] = announcement.radio_media_announcement[0].radio_media_announcement_time_slot[0].time_slot
		p.append(k)
		
	return jsonify({'announcements':p})
		
	