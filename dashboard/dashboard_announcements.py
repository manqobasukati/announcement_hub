from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from dashboard import dashboard_print
from app import db
from random import randint
from models import Announcement,User, PrintMediaAnnouncement, Media, RadioMediaAnnouncement,RadioMediaAnncouncemntFuneral
from forms import AnnouncementCriteriaPrint, AnnouncementCriteriaRadio
import datetime
from datetime import date



@dashboard_print.route("/announcements", methods=['GET','POST'])
@login_required
def dashboard_announcements_view():
	title = "Anncouncements"
	announcements = []
	id = current_user.get_id()
	media = Media.query.filter_by(id=id).first()
	if media.media_type == 'radio_media':
	
		for a in Announcement.query.filter_by(media_id=media.id).all():
			for b in a.radio_media_announcement:
				if b.date == str(datetime.date.today()) and b.read ==  False:
					announcements.append(b)
			
			for c in a.radio_media_funeral_announcement:
				if c.date == str(datetime.date.today()) and c.read == False:
					announcements.append(c)
		print(announcements)		
		if request.method == 'POST':
			if request.form['announcement_type'] == 'funeral':
				announcements = RadioMediaAnncouncemntFuneral.query.filter(
									 (RadioMediaAnncouncemntFuneral.date==str(request.form['announcement_date']))&
										(RadioMediaAnncouncemntFuneral.media_id==media.id) & 
											(RadioMediaAnncouncemntFuneral.type==request.form['announcement_type']) & 
												(RadioMediaAnncouncemntFuneral.time_slot==request.form['time_slot'])).all()
				return render_template("dashboard/dashboard_home_for_radio_media.html",media_name=media.media_name,announcements=announcements)
			elif request.form['announcement_type'] == ('sports' or 'cars'):
				announcements = RadioMediaAnnouncement.query.filter(
										 (RadioMediaAnnouncement.date==str(request.form['announcement_date']))&
											(RadioMediaAnnouncement.media_id==media.id) & 
												(RadioMediaAnnouncement.type==request.form['announcement_type']) & 
													(RadioMediaAnnouncement.time_slot==request.form['time_slot'])).all()
		return render_template("dashboard/dashboard_home_for_radio_media.html",media_name=media.media_name,announcements=announcements)
	elif media.media_type == 'print_media':
		"""
		announcements = PrintMediaAnnouncement.query.filter(
							(Announcement.media_id == media.id)
								(str(Announcement.start_day)[0:10] == str(datetime.date.today()))
								).all() 
		"""
		announcements = []
		for a in PrintMediaAnnouncement.query.filter(Announcement.media_id == media.id).all():
			if str(a.print_media_announcement.start_day)[0:10] == str(datetime.date.today()) and a.print_media_announcement.announced == False:
				announcements.append(a)
		if request.method == 'POST':
			announcements = []
			for b in PrintMediaAnnouncement.query.filter(Announcement.media_id == media.id).all():
				if (request.form['announcement_date'] == str(b.print_media_announcement.start_day)[0:10]) and (request.form['announcement_section'] == b.section)  and (b.print_media_announcement.announced == False):
					print("True")
					announcements.append(b)
		return render_template("dashboard/dashboard_home_for_print_media.html",media_name=media.media_name,announcements=announcements)
							


@dashboard_print.route("/announcements/<type>/<int:id>", methods=['GET','POST'])
def dashboard_single_announcement_view(type,id):
	if type == 'funeral':
		announcement = RadioMediaAnncouncemntFuneral.query.filter_by(id=id).first()
		message = ''
		if request.method == 'POST':
			announcement.read = True
			db.session.add(announcement)
			db.session.commit()
			message = 'Announcement succesfully read'
			return render_template('dashboard/single_funeral_announcement.html', announcement=announcement,message=message)
		return render_template('dashboard/single_funeral_announcement.html', announcement=announcement)
	else:
		announcement = RadioMediaAnnouncement.query.filter_by(id=id).first()
		message = ''
		if request.method == 'POST':
			announcement.read = True
			db.session.add(announcement)
			db.session.commit()
			message = 'Announcement succesfully read'
			return render_template('dashboard/single_radio_announcement.html', announcement=announcement,message=message)
		return render_template('dashboard/single_radio_announcement.html', announcement=announcement)
		
@dashboard_print.route("/announcements/print/<type>/<int:id>", methods=['GET','POST'])
def dashboard_single_print_announcement_view(type,id):
	announcement = PrintMediaAnnouncement.query.filter_by(id=id).first()
	message = ''
	if request.method == 'POST':
		announcement.print_media_announcement.announced = True
		db.session.add(announcement)
		db.session.commit()
		message = 'Announcement succesfully read'
		return render_template('dashboard/single_print_announcement.html', announcement=announcement,message=message)
	return render_template('dashboard/single_print_announcement.html', announcement=announcement)
	

	

	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	