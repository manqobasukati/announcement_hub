from api import api_print
from flask import request,jsonify
from app import db, bcrypt
from models import User

@api_print.route('/user-registration', methods=['POST','GET'])
def user_registration_view():

	#Check to see if method is post, then get inputed fields
	if request.method == 'POST':
		content = request.get_json(force=True)
		user_name = content["user_name"]
		user_surname = content["user_surname"]
		user_email = content["user_email"]
		user_password = content["user_password"]
		user_phone_number = content["user_phone_number"]
		user_middle_name = content["user_middle_name"]
		user_postal_address = content["user_postal_address"]
		user_national_id_number = content["user_national_id_number"]
		if User.query.filter_by(user_national_id_number=user_national_id_number).first() is not None:
			print(User.query.filter_by(user_national_id_number=user_national_id_number).first())
			return jsonify({'message':'user already exists'})
		if (user_name or user_surname or user_email or user_password or user_phone_number or user_national_id_number ) == None:
			return jsonify({'message':'missing data fields'})
		else:
			#First encrypt password 
			user_password_hash = bcrypt.generate_password_hash(user_password)
			user = User(user_name=user_name,user_email=user_email,user_phone_number=user_phone_number,user_national_id_number=user_national_id_number,user_password_hash=user_password_hash,user_surname=user_surname,user_middle_name=user_middle_name,user_postal_address=user_postal_address)
			db.session.add(user)
			db.session.commit()
			return jsonify({'message':'succesfully registered'})
			
	
		