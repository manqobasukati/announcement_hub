from account import account_print
from flask import render_template, request, url_for, redirect
from flask_login import login_user, current_user, login_required, logout_user
from forms import MediaSignInForm
from app import bcrypt
from models import Media
from functools import wraps




#@account_print.route("/accounts/sign-in")
@account_print.route("/sign-in", methods=['GET','POST'])
def sign_in_view():
	title = "Sign in"
	message = ""
	form = MediaSignInForm()
	
	if request.method == "POST":
		email = form.media_email.data
		if Media.query.filter_by(media_email=email).first() is None:
			message = "Account does not exist"
			return render_template("accounts/sign_in_page.html",title=title, form=form, message=message)
		media = Media.query.filter_by(media_email=email).first()
		if not bcrypt.check_password_hash(media.media_password, form.media_password.data):
			message = "Pasword is not correct"
			return render_template("accounts/sign_in_page.html",title=title, form=form, message=message)
		message =  "Successfull login"
		login_user(media)
		return redirect('/dashboard/announcements')
		#return render_template("accounts/sign_in_page.html",title=title, form=form, message=message)
		
	
	return render_template("accounts/sign_in_page.html",title=title, form=form)
	
	
	
@account_print.route('/logout')
@login_required
def logout_view():
	logout_user()
	return redirect(url_for('home_print.home_page'))