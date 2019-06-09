from flask import Blueprint

account_print = Blueprint('account_print', __name__,
template_folder='templates',url_prefix="/accounts")


#from account.account_print import *
from account.accounts_sign_up import *
from account.accounts_sign_in import *


