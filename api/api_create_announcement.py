#Create an announcement
from datetime import datetime
#import datetime
from api import api_print
#from api.api_user_login import *
from flask import request,jsonify, url_for
import requests, urllib
from app import db
from models import Announcement,AnnouncementType, RadioMediaAnncouncemntFuneral, Media,RadioMediaAnnouncementCharge, RadioMediaAnnouncement, PrintMediaAnnouncement,PrintMediaAnnouncementCharge
from api import token_required
from sqlalchemy.exc import IntegrityError
from api.functions import dates, create_radio_normal_announcemnet_bill,create_print_announcement_bill


def string_to_date(date):
	day = date[0:2]
	month = date[3:5]
	year = date[6:10]
	return datetime(int(year),int(month),int(day))
	
"""
def dates(start_day,end_day):
	start = datetime.datetime.strptime(start_day, "%d-%m-%Y")
	end = datetime.datetime.strptime(end_day, "%d-%m-%Y")
	date_array = (start + datetime.timedelta(days=x) for x in range(0, (end-start).days+1))
	my_list = []
	for date_object in date_array:
		my_list.append(date_object.strftime("%d-%m-%Y"))
	return my_list
"""




@api_print.route('/all-media-houses',methods=['POST','GET'])
def expose_all_media_houses():
	media = Media.query.all()
	#print(media)
	m = []
	#p = []
	j = 0
	for i in media:
		k = {}
		p = []
		k['media_id'] = i.id
		k['media_name'] = i.media_name		
		for r in AnnouncementType.query.filter_by(media_id=i.id).all():
			p.append(r.type_name)
		k['announcement_type'] = p
		m.append(k)
		
		

	return jsonify(m)
"""
"""	
@api_print.route('/status', methods=['GET','POST'])
def status_view():
	data = request.json
	if request.method == 'POST':
		p = []
		j = 0
		for announcement in Announcement.query.filter_by(user_id=data['user_id']).all():
			k = {}
			k['from_date'] = announcement.start_day
			k['to_date'] = announcement.end_day
			k['id'] = announcement.id
			k['read'] = announcement.announced
			
			
			if announcement.radio_media_announcement is not None:
				k['radio_announcements'] = []
				for i in announcement.radio_media_announcement:
					u = {}
					u['read'] = i.read
					u['id']  = i.id
					u['contact'] = i.contact
					k['radio_announcements'].append(u)
				
				
				if len(k['radio_announcements']) == 0:
					del k['radio_announcements']
				
			if announcement.radio_media_funeral_announcement is not None:
				k['radio_funeral_announcements'] = []
				for i in announcement.radio_media_funeral_announcement:
					u = {}
					u['read'] = i.read
					u['id']  = i.id
					u['contact'] = i.contact
					k['radio_funeral_announcements'].append(u)
					
				if len(k['radio_funeral_announcements']) == 0:
					del k['radio_funeral_announcements']
					
			if announcement.print_media_announcement is not None:
				k['print_media_announcement'] = {}
				for i in announcement.print_media_announcement:
					k['print_media_announcement']['id'] = i.id 
					k['print_media_announcement']['content'] = i.content
				
				if len(k['print_media_announcement']) == 0:
					del k['print_media_announcement']
				
			
			p.append(k)
			
		
		
		return jsonify(p)
"""
"""	
@api_print.route('/create-radio-normal-announcement-bill',methods=['POST','GET'])
def create_radio_normal_announcemnet_view_bill():
	data = request.json
	if request.method == 'POST':
		days = string_to_date(data['to_date']) - string_to_date(data['from_date'])
		days_in_str = str(days)
		content = days_in_str.split(' ')
		total_time_slots = int(content[0]) * len(data['time_slots'])
		charge_db = RadioMediaAnnouncementCharge.query.filter_by(media_id=data['media_id']).first()
		total_charge = charge_db.charge_per_time_slot * total_time_slots
		return jsonify({'total_charge':total_charge})

	

	

@api_print.route('/create-radio-normal-announcement',methods=['POST','GET'])
#@token_required
def create_radio_normal_announcement_view():
	data = request.json
	if request.method == 'POST':
		json = {'to_date':data['to_date'],'from_date':data['from_date'],'time_slots':data['time_slots'],'media_id':data['media_id']}
		announcement = Announcement(announcement_type='radio_media',start_day=string_to_date(data['from_date']),
						end_day=string_to_date(data['to_date']),user_id=data['user_id'],media_id=data['media_id'],paid=False,announced=False)
		announcement.no_of_days = string_to_date(data['to_date']).day - string_to_date(data['from_date']).day
		announcement.charge = create_radio_normal_announcemnet_bill(data)
		db.session.add(announcement)
		db.session.commit()
		start_day = data['from_date']
		end_day = data['to_date']
		for i in dates(start_day,end_day):
			for j in data['time_slots']:
				radio_announce = RadioMediaAnnouncement(contact=data['contact'],type=data['type'],content=data['content'],
										media_id=data['media_id'],announcement_id=announcement.id,date=str(string_to_date(i))[0:10], time_slot=j)
				db.session.add(radio_announce)
				db.session.commit()
		
		return jsonify({'message':'sucessfully created radio announcement'})
		
		
		



	
@api_print.route('/create-radio-funeral-announcement',methods=['POST','GET'])
#@token_required
def create_radio_funeral_announcemnet_view():
	data = request.json
	if request.method == 'POST':
		json = {'to_date':data['to_date'],'from_date':data['from_date'],'time_slots':data['time_slots'],'media_id':data['media_id']}
		announcement = Announcement(announcement_type='radio_media',start_day=string_to_date(data['from_date']),
						end_day=string_to_date(data['to_date']),user_id=data['user_id'],media_id=data['media_id'],announced=False,paid=False)
		announcement.charge = create_radio_normal_announcemnet_bill(data)
		db.session.add(announcement)
		db.session.commit()
		start_day = data['from_date']
		end_day = data['to_date']
		for i in dates(start_day,end_day):
			for j in data['time_slots']:
				radio_announce = RadioMediaAnncouncemntFuneral(contact=data['contact'],
										announcement_id=announcement.id,deceased_name=data['deceased_name'],
										deceased_other_name=data['deceased_other_name'],
										funeral_venue=data['funeral_venue'],vigil_venue=data['vigil_venue'],
										media_id=data['media_id'],date=str(string_to_date(i))[0:10], time_slot=j)
				db.session.add(radio_announce)
				db.session.commit()
		
		return jsonify({'message':'sucessfully created radio announcement'})


		
	
	
	
@api_print.route('/create-print-announcement-bill', methods=['GET','POST'])
def create_print_announcement_bill_view():
	data = request.json
	if request.method == 'POST':
		content_count =  len(data['content'].split())
		content_count = content_count + 1#for contact
		days = string_to_date(data['to_date']) - string_to_date(data['from_date'])
		days_in_str = str(days)
		content = days_in_str.split(' ')
		no_of_days = int(content[0])
		charge_db = PrintMediaAnnouncementCharge.query.filter_by(media_id=data['media_id']).first()
		total = total_charge(no_of_days,content_count,charge_db.charge_per_word,charge_db.per_pic,data['picture'])
		return jsonify({'total_charge':total})
		
	
@api_print.route('/create-print-announcement', methods=['GET','POST'])
#@token_required
def create_print_announcement_view():#current_user):
	data = request.json
	if request.method == 'POST':
		json = {'to_date':data['to_date'],'from_date':data['from_date'],'content':data['content'],'picture':data['picture'],'media_id':data['media_id']}
		try:
			announcement = Announcement(
							announcement_type='print_media',
							user_id=int(data['user_id']),media_id=int(data['media_id']),
							announced=False,paid=False, 
							start_day=string_to_date(data['from_date']),
							end_day=string_to_date(data['to_date'])
							)
			announcement.charge = create_print_announcement_bill(data)
			
			db.session.add(announcement)
			db.session.commit()
		except IntegrityError:
			return jsonify({'message':'Database integrity error'})
		
		days = string_to_date(data['to_date']) - string_to_date(data['from_date'])
		days_in_str = str(days)
		content = days_in_str.split(' ')
		no_of_days = int(content[0])
		
		try:
			p_announcement = PrintMediaAnnouncement(
								announcement_id=announcement.id,
								section=data['type'],
								contact=data['contact'],
								content = data['content'],
								picture=data['picture'])
								
			p_announcement.number_of_days = int(content[0])
			db.session.add(p_announcement)
			db.session.commit()
		except IntegrityError:
			return jsonify({'message':'Database integrity error'})
		
		return jsonify({'message':'successfully submited print media announcement'})

