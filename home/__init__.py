from flask import Blueprint

home_print = Blueprint('home_print', __name__,
template_folder='templates')


from home.home_page import *


