import datetime
from flask import jsonify
from models import RadioMediaAnnouncementCharge, PrintMediaAnnouncementCharge


def total_charge(no_of_days, content_count, charge_per_word,per_pic,pic):
	total = 0
	if pic == '':
		total = no_of_days * (content_count*charge_per_word + per_pic )
	elif pic != '':
		total = no_of_days * (content_count*charge_per_word)
	return total 

def string_to_date(date):
	from datetime import datetime
	day = date[0:2]
	month = date[3:5]
	year = date[6:10]
	return datetime(int(year),int(month),int(day))




def dates(start_day,end_day):
	start = datetime.datetime.strptime(start_day, "%d-%m-%Y")
	end = datetime.datetime.strptime(end_day, "%d-%m-%Y")
	date_array = (start + datetime.timedelta(days=x) for x in range(0, (end-start).days+1))
	my_list = []
	for date_object in date_array:
		my_list.append(date_object.strftime("%d-%m-%Y"))
	return my_list
	
def create_radio_normal_announcemnet_bill(data):
	days = string_to_date(data['to_date']) - string_to_date(data['from_date'])
	days_in_str = str(days)
	content = days_in_str.split(' ')
	total_time_slots = int(content[0]) * len(data['time_slots'])
	charge_db = RadioMediaAnnouncementCharge.query.filter_by(media_id=data['media_id']).first()
	total_charge = charge_db.charge_per_time_slot * total_time_slots
	return total_charge
	
def create_print_announcement_bill(data):
	content_count =  len(data['content'].split())
	content_count = content_count + 1#for contact
	days = string_to_date(data['to_date']) - string_to_date(data['from_date'])
	days_in_str = str(days)
	content = days_in_str.split(' ')
	no_of_days = int(content[0])
	charge_db = PrintMediaAnnouncementCharge.query.filter_by(media_id=data['media_id']).first()
	total = total_charge(no_of_days,content_count,charge_db.charge_per_word,charge_db.per_pic,data['picture'])
	return total
		
	
	
"""
for date_object in dates("12-12-2016","12-12-2016"):
    print(date_object.strftime("%d-%m-%Y"))
"""
	


	
	
	

