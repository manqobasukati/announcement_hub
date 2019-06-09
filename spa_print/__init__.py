from flask import Blueprint


spa_print = Blueprint('spa_print', __name__,url_prefix='/spa/')

from spa_print.spa_print_home import *
