from api import api_print
from api.api_user_login import *
from flask import request,jsonify
from flask_mail import Message
from app import mail, app,bcrypt,db
from random import randint
from models import User


@api_print.route("/user-recover-password", methods=["GET","POST"])
def user_recover_password_view(current_user):
	#email = request.args.get('user_email')
	content = request.json
	user_phone_number = content["user_phone_number"]
	if User.query.filter_by(user_phone_number=user_phone_number).first() is not None:
		random_pass = randint(1000,9999)
		user = User.query.filter_by(user_phone_number=user_phone_number).first()
		user.user_password_hash = bcrypt.generate_password_hash(str(random_pass))
		db.session.commit()
		msg = Message(subject='Announcement hub password recovery',sender=app.config.get("MAIL_USERNAME"), recipients=[user.user_email],body="This is your password {}".format(str(random_pass)))
		mail.send(msg)
		return jsonify({'message':'password sent to  email'})
	elif User.query.filter_by(user_phone_number=user_phone_number).first() is None:
		return jsonify({'message':'password not sent, invalid phone number'})
	
	

