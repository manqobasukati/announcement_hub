from flask import Blueprint


api_print = Blueprint('api_print', __name__,url_prefix='/api/v1/')


from api.api_user_registration import *
from api.api_user_login import *
from api.api_user_recover_password import *
from api.api_create_announcement import *
from api.api_edit_user import *
	
	