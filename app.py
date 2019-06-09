from flask import Flask
from config import *
from flask_bcrypt import Bcrypt
from flask_migrate import  Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager
from flask_mail import Mail
from flask_admin.contrib.sqla import ModelView
import os


mail_settings = { "MAIL_SERVER":'smtp.gmail.com',"MAIL_PORT":465,"MAIL_USE_TLS":False,"MAIL_USE_SSL":True,"MAIL_USERNAME":'manqobasukzin27@gmail.com',"MAIL_PASSWORD":'france12'}



app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
app.config.update(mail_settings)


#libraries to be used
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
admin = Admin(app)
login_manager = LoginManager(app)
mail = Mail(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db',MigrateCommand)


from admin import *

from home import home_print
from account import account_print
from api import api_print
from dashboard import dashboard_print
from spa_print import spa_print



app.register_blueprint(home_print)
app.register_blueprint(account_print)
#app.register_blueprint(api_print)
#app.register_blueprint(dashboard_print)
#app.register_blueprint(spa_print)






if __name__ == '__main__':
	#admin.init_app(app)
	#manager.run()
	app.run()