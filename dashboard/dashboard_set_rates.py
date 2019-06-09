from flask import render_template, redirect, url_for, request
from dashboard import dashboard_print
from forms import PrintSetRatesForm, RadioSetRatesForm
from flask_login import login_required, current_user
from models import  PrintMediaAnnouncementCharge, RadioMediaAnnouncementCharge
from app import db


@dashboard_print.route("/set-rates", methods=['GET','POST'])
@login_required
def dashboard_set_rates_view():
	title = "Set rates"
	if current_user.media_type == 'print_media':
		form = PrintSetRatesForm()
		message = ''
		if request.method == 'POST':
			print_media = PrintMediaAnnouncementCharge(media_id=current_user.id,charge_per_word=form.charge_per_word.data, charge_per_day = form.charge_per_day.data, per_pic = form.charge_per_pic.data)
			db.session.add(print_media)
			db.session.commit()
			message = 'Successfully changed charge rates'
		return render_template("dashboard/dashboard_set_rates_page.html",title=title, form=form, message=message)
	elif current_user.media_type == 'radio_media':
		form = RadioSetRatesForm()
		message = ''
		if request.method == 'POST':
			radio_media = RadioMediaAnnouncementCharge(media_id=current_user.id, charge_per_time_slot = form.charge_per_slot.data)
			db.session.add(radio_media)
			db.session.commit()
			message = 'Successfully changed charge rates'
		return render_template("dashboard/dashboard_set_rates_page.html",title=title, form=form, message=message )
	return render_template("dashboard/dashboard_set_rates_page.html",title=title)