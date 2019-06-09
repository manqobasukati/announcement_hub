from flask import Blueprint

dashboard_print = Blueprint('dashboard_print', __name__,
template_folder='templates',url_prefix='/dashboard/')

from dashboard.dashboard_home import *
from dashboard.dashboard_announcements import *
from dashboard.dashboard_profile import *
from dashboard.dashboard_transactions import *
from dashboard.dashboard_set_rates import *
from dashboard.dashboard_api import *

