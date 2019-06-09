from flask import render_template, redirect, url_for, request,flash
from account import account_print
from forms import MediaSignUpForm
from app import db, bcrypt, mail,app
from models import Media
from flask_mail import Message


@account_print.route("/sign-up",methods=['GET','POST'])
def sign_up_view():
	title = "Sign up page"
	form = MediaSignUpForm()
	"""
	if form.media_name is not None:
		return redirect(url_for('account_print.success_sign_up_view'))
	"""
	if request.method =='POST':
		name = form.media_name.data
		type = form.media_type.data
		email = form.media_email.data
		if Media.query.filter_by(media_name=name).first() is not None:
			message = "Media house already exists"
			return render_template("accounts/sign_up_page.html",title=title,form=form,message=message)
		password =  bcrypt.generate_password_hash(form.media_password.data).decode('utf-8')
		media = Media(media_name=name,media_type=type,media_email=email,media_password=password)
		db.session.add(media)
		db.session.commit()
		media_id = media.id
		message = "Please confirm email to complete sign up "
		link = '<html><head><title>C Email</title></head><body><a href="http://127.0.0.1:5000/accounts/email-confirmation/{}">Confirm</a></body></html>'.format(str(media_id))
		msg = Message(subject='Announcement Media confirmation',sender=app.config.get("MAIL_USERNAME"), recipients=[email],body="Click here to confirm email {}".format(link))
		mail.send(msg)
		""""if (name or email or type) == None:
			return return render_template("accounts/sign_up_page.html",title=title,form=form,error)"""

		return render_template("accounts/sign_up_page.html",title=title,form=form, message=message,media_id=media_id)
	else:
		return render_template("accounts/sign_up_page.html",title=title,form=form)
	
#msg = Message(subject='Announcement hub password recovery',sender=app.config.get("MAIL_USERNAME"), recipients=[user.user_email],body="This is your password {}".format(str(random_pass)))
#mail.send(msg)	
	
@account_print.route("/success-sign-up/")
def success_sign_up_view():
	title = "Successfully sign up"
	return render_template("accounts/success_sign_up_page.html",title=title)
	
@account_print.route("/email-confirmation/<int:media_id>")
def email_confirmation_view(media_id):
	media = Media.query.filter_by(id=media_id).first()
	media.email_confirmation = True
	db.session.commit()
	return redirect(url_for('account_print.success_sign_up_view'))
	