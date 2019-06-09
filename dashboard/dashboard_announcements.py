from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from dashboard import dashboard_print
from app import db
from random import randint
from models import Announcement,User, PrintMediaAnnouncement, Media, RadioMediaAnnouncementTimeSlot, RadioMediaAnnouncement
from forms import AnnouncementCriteriaPrint, AnnouncementCriteriaRadio
import datetime
from datetime import date


@dashboard_print.route("/announcements", methods=['GET','POST'])
@login_required
def dashboard_announcements_view():
	title = "Anncouncements"
	media = Media.query.filter_by(id=current_user.id).first()
	#announcements = Announcement.query.filter_by(media_id=media.id).all()
	if media.media_type == 'print_media':
		#form = AnnouncementCriteriaPrint()
		announcements = Announcement.query.filter_by(media_id=media.id).all()
		start = date(year=2019,month=2,day=14)
		end = date(year=2019,month=2,day=14)
		p = Announcement.query.filter(Announcement.start_day == start).all()
		print(p)
		if request.method == 'POST':
			announcements = Announcement.query.filter_by(announced = int(form.announced.data)).all()
		return render_template("dashboard/dashboard_announcements_page.html",title=title, announcements=announcements,media=media,form=form)
	elif media.media_type == 'radio_media':
		form = AnnouncementCriteriaRadio()
		x = datetime.datetime.now()
		#start = date(year=x.year,month=x.month,day=x.day)
		#end = date(year=x.year,month=x.month,day=x.day+1)
		#print(str(x)[0:10])
		#p = Announcement.query.filter(Announcement.start_day >= start).filter(Announcement.start_day <= end).filter_by(media_id=media.id).all()
		first_time_slot = []
		
		second_time_slot = []
		for i in Announcement.query.filter_by(media_id=media.id).all():
			if str(i.start_day)[0:10] == str(x)[0:10]:
				#no_of_days = i.end_day.day - i.start_day.day
				#i.start_day 
				#print(no_of_days)
				for k in i.radio_media_announcement:
					for j in k.radio_media_announcement_time_slot:
						if j.time_slot == "10:30":
							first_time_slot.append(i)
						elif j.time_slot == "5:30":
							second_time_slot.append(i)
						
		r_a = RadioMediaAnnouncement.query.filter_by(media_id=media.id).all()
		print(first_time_slot)
		print(second_time_slot)
		return render_template("dashboard/dashboard_announcements_page.html",title=title,today=str(x)[0:10],first_time_slot=first_time_slot,second_time_slot=second_time_slot,media=media,form=form)
		
	#user = User.query.filter_by(user_id=announcements.user_id).first()
	#print_media  = PrintMediaAnnouncement.query.filter_by(announcement_id=1).first()
	return render_template("dashboard/dashboard_announcements_page.html",title=title)
	



	
	
@dashboard_print.route("/announcements/<int:id>/<int:time_slot_id>/<string:time_slot>", methods=['GET','POST'])
def dashboard_single_announcement_view(id,time_slot_id,time_slot):
	a = Announcement.query.filter_by(id=id).first()
	message = ''
	link = '/dashboard/announcements/'+str(id)+'/'+str(time_slot_id)+'/'+time_slot
	ra = RadioMediaAnnouncement.query.filter_by(announcement_id=a.id).first()
	tm = RadioMediaAnnouncementTimeSlot.query.filter_by(radio_media_announcement_id=ra.id,id=time_slot_id,time_slot=time_slot).first()
	#print(link)
	if request.method == 'POST':
		if a.announcement_type == 'radio_media':
			message = 'Succesfully announced announcement'
			ra = RadioMediaAnnouncement.query.filter_by(announcement_id=a.id).first()
			a.no_of_days = a.no_of_days - 1
			a.start_day = date(year=a.start_day.year,month=a.start_day.month,day = a.start_day.day + 1)
			#tm.read = True
			ra = RadioMediaAnnouncement.query.filter_by(announcement_id=a.id).first()
			tm = RadioMediaAnnouncementTimeSlot.query.filter_by(radio_media_announcement_id=ra.id,id=time_slot_id,time_slot=time_slot).first()
			if a.no_of_days != 0:
				tm.read = False
				a.announced = False
				db.session.commit()
			else:
				tm.read = True
				db.session.commit()
			
			if tm.read is True:
				a.announced = True
				db.session.commit()
			#db.session.delete(tm)
			
			db.session.commit()
			return render_template("dashboard/dashboard_single_announcement_page.html", a=a,tm=tm,message=message)
	return render_template("dashboard/dashboard_single_announcement_page.html", a=a, tm=tm,link=link,message=message)
	
	

	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	