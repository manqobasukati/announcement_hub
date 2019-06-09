#Create an announcement

from api import api_print
from api.api_user_login import *
from flask import request,jsonify, url_for
import requests, urllib
from datetime import datetime
from models import Announcement,AnnouncementType, RadioMediaAnncouncemntFuneral, Media,RadioMediaAnnouncementCharge, RadioMediaAnnouncement,RadioMediaAnnouncementTimeSlot, PrintMediaAnnouncement,PrintMediaAnnouncementCharge
from api import token_required
from sqlalchemy.exc import IntegrityError


def string_to_date(date):
	day = date[0:2]
	month = date[3:5]
	year = date[6:10]
	return datetime(int(year),int(month),int(day))

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

		
@api_print.route('/status', methods=['GET','POST'])
def status_view():
	data = request.json
	if request.method == 'POST':
		p = []
		i = 0
		print(data['user_id'])
		for announcement in Announcement.query.filter_by(user_id=data['user_id']).all():
			k = {}
			k['from_date'] = announcement.start_day
			k['to_date'] = announcement.end_day
			k['id'] = announcement.id
			k['read'] = announcement.announced
			#print(announcement.radio_media_announcement[0].radio_media_announcement_time_slot[0].time_slot)
			if announcement.radio_media_announcement:
				k['time_slot'] = announcement.radio_media_announcement[0].radio_media_announcement_time_slot[0].time_slot
			p.append(k)
		
		"""		
		for announcement in Announcement.query.filter_by(user_id=data['user_id']).all():
			k = {}
			k['from_date'] = announcement.start_day
			k['to_date'] = announcement.end_day
			k['id'] = announcement.id
			k['read'] = announcement.announced
			#print(announcement.radio_media_announcement[0].radio_media_announcement_time_slot[0].time_slot)
			if announcement.radio_media_announcement:
				k['time_slot'] = announcement.radio_media_announcement[0].radio_media_announcement_time_slot[1].time_slot
			p.append(k)
		"""	
		return jsonify(p)
	
@api_print.route('/create-radio-normal-announcement-bill',methods=['POST','GET'])
def create_radio_normal_announcemnet_view_bill():
	data = request.json
	date = "2018-12-02"
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
def create_radio_normal_announcement_view():#current_user):
	data = request.json
	if request.method == 'POST':
		json = {'to_date':data['to_date'],'from_date':data['from_date'],'time_slots':data['time_slots'],'media_id':data['media_id']}
		#r = requests.post('http://127.0.0.1:5000/api/v1/create-radio-normal-announcement-bill',json=json,proxies={'http':None})
		#d = r.json()
		#print(d)
		announcement = Announcement(announcement_type='radio_media',start_day=string_to_date(data['from_date']),end_day=string_to_date(data['to_date']),user_id=data['user_id'],media_id=data['media_id'],paid=False,announced=False)
		announcement.no_of_days = string_to_date(data['to_date']).day - string_to_date(data['from_date']).day
		print(string_to_date(data['to_date']).day - string_to_date(data['from_date']).day)
		#announcement.charge = d['total_charge']
		db.session.add(announcement)
		db.session.commit()
		radio_announce = RadioMediaAnnouncement(contact=data['contact'],type=data['type'],content=data['content'],media_id=data['media_id'],announcement_id=announcement.id)
		db.session.add(radio_announce)
		db.session.commit()
		for i in data['time_slots']:
			time_s = RadioMediaAnnouncementTimeSlot(time_slot=i,radio_media_announcement_id=radio_announce.id)
			db.session.add(time_s)
			db.session.commit()
		return jsonify({'message':'sucessfully created radio announcement'})
		
		
		



	
@api_print.route('/create-radio-funeral-announcement',methods=['POST','GET'])
#@token_required
def create_radio_funeral_announcemnet_view():#current_user):
	data = request.json
	if request.method == 'POST':
		json = {'to_date':data['to_date'],'from_date':data['from_date'],'time_slots':data['time_slots'],'media_id':data['media_id']}
		r = requests.post('http://announcementhub.pythonanywhere.com/api/v1/create-radio-normal-announcement-bill',json=json,proxies={'http':None})
		d = r.json()
		print(d)
		announcement = Announcement(announcement_type='radio_media',user_id=data['user_id'],media_id=data['media_id'],announced=False,paid=False)
		announcement.charge = d['total_charge']
		db.session.add(announcement)
		db.session.commit()
		r_f_announcement = RadioMediaAnncouncemntFuneral(announcement_id=announcement.id,deceased_name=data['deceased_name'],deceased_other_name=data['deceased_other_name'],funeral_venue=data['funeral_venue'],vigil_venue=data['vigil_venue'])
		db.session.add(r_f_announcement)
		db.session.commit()
		for i in data['time_slots']:
			time_s = RadioMediaAnnouncementTimeSlot(time_slot=i,radio_media_announcement_id=r_f_announcement.id)
			db.session.add(time_s)
			db.session.commit()
		return jsonify({'message':'successfully submited funeral announcement'})
	return jsonify({'message':'just a get request user'})
	


def total_charge_(no_of_days, content_count, charge_per_word,per_pic,pic):
	total = 0
	if pic == '':
		total = no_of_days * (content_count*charge_db.charge_per_word + charge_db.per_pic )
	elif pic != '':
		total = no_of_days * (content_count*charge_db.charge_per_word)
	return total 
		
	
	
	
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
		print("Send 2")
		r = requests.post('http://announcementhub.pythonanywhere.com/api/v1/create-print-announcement-bill',json=json,proxies={'http':None})
		print("Send 3")
		d = r.json()
		print(data['from_date'])
		
		try:
			announcement = Announcement(
							announcement_type='print_media',
							user_id=int(data['user_id']),media_id=int(data['media_id']),
							announced=False,paid=False, 
							start_day=string_to_date(data['from_date']),
							end_day=string_to_date(data['to_date'])
							)
			announcement.charge = d['total_charge']
			
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
								section=data['section'],
								contact=data['contact'],
								picture=data['picture'])
								
			p_announcement.number_of_days = int(content[0])
			db.session.add(p_announcement)
			db.session.commit()
		except IntegrityError:
			return jsonify({'message':'Database integrity error'})
		
		return jsonify({'message':'successfully submited print media announcement'})