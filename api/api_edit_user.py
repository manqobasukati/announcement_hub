from api import api_print
from flask import request,jsonify
from app import db, bcrypt
from models import User
from api import token_required

@api_print.route('/user-edit', methods=['POST','GET','PUT'])
@token_required 
def user_edit_view(current_user):

	#Check to see if method is post, then get inputed fields
	if request.method == 'PUT':
		content = request.get_json(force=True)
		user = User.query.filter_by(user_id=current_user.user_id).first()
			#for i in user:
		if user.user_email == content['user_email']:
			user.user_email = user.user_email
		else:
			if User.query.filter_by(user_email = content['user_email']).first() is not None:
				return jsonify({'message':'email already exist'})
			else:
				user.user_email = content['user_email']
				
		if user.user_phone_number == content['user_phone_number']:
			user.user_phone_number = user.user_phone_number
		else:
			if User.query.filter_by(user_phone_number = content['user_phone_number']).first() is not None:
				return jsonify({'message':'phone number already exist'})
			else:
				user.user_phone_number = content['user_phone_number']
				
		if user.user_national_id_number == content['user_national_id_number']:
			user.user_national_id_number = user.user_national_id_number
		else:
			if User.query.filter_by(user_national_id_number = content['user_national_id_number']).first() is not None:
				return jsonify({'message':'national id number already exist'})
			else:
				user.user_national_id_number = content['user_national_id_number']
		user.user_name = content['user_name']
		user.user_middle_name = content['user_middle_name']
		user.user_postal_address = content['user_postal_address']
		user.user_password_hash = bcrypt.generate_password_hash(content['user_password'])
		if content['password_recovered'] == "True":
			user.password_recovered = True
		elif content['password_recovered'] == "False":
			user.password_recovered = False
		db.session.commit()
		return jsonify({'message':'succesfully updated user'})
		
			
			
					
					
			
			