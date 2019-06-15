from flask import render_template, redirect, url_for, request
from dashboard import dashboard_print
from forms import PrintSetRatesForm, RadioSetRatesForm
from flask_login import login_required, current_user
from models import  PrintMediaAnnouncementCharge, RadioMediaAnnouncementCharge, Media
from app import db


@dashboard_print.route("/set-rates", methods=['GET','POST'])
#@login_required
def dashboard_set_rates_view():
	title = "Set rates"
	message = ''
	current_user = Media.query.filter_by(id=2).first()
	media_name = current_user.media_name
	if current_user.media_type == 'print_media':
		if request.method == 'POST':
			if PrintMediaAnnouncementCharge.query.filter_by(media_id = current_user.id).first() is not None:
				p = PrintMediaAnnouncementCharge.query.filter_by(media_id = current_user.id).first()
				p.charge_per_word = request.form['charge_per_word']
				p.charge_per_day = request.form['charge_per_day']
				p.charge_per_pic = request.form['charge_per_pic']
				db.session.commit()
				message = 'Successfully  updated charges'
			else:
				charge = PrintMediaAnnouncementCharge()
				charge.charge_per_word = request.form['charge_per_word']
				charge.charge_per_day = request.form['charge_per_day']
				charge.charge_per_pic = request.form['charge_per_pic']
				db.session.commit()
				message = 'Successfully  created charges'
		return render_template("dashboard/account_charges_print.html",title=title, message=message,media_name=media_name)
	elif current_user.media_type == 'radio_media':
		if request.method == 'POST':
			if RadioMediaAnnouncementCharge.query.filter_by(media_id=current_user.id).first()is not None:
				r =  RadioMediaAnnouncementCharge.query.filter_by(media_id=current_user.id).first()
				r.charge_per_time_slot = request.form['charge_time_slot']
				db.session.commit()
				message = 'Succesfully updated charges'
			else:
				charge = RadioMediaAnnouncementCharge(media_id=current_user.id, charge_per_time_slot = request.form['charge_time_slot']) 
				db.session.add(charge)
				db.session.commit()
				message = 'Succesfully created charges'
		return render_template("dashboard/account_charges.html",title=title, message=message,media_name=media_name)
	return render_template("dashboard/account_charges.html",title=title, media_name=media_name)