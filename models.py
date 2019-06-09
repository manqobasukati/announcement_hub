import datetime, re
from app import db,login_manager,bcrypt
from flask_login import UserMixin


class User(db.Model):
	__tablename__ = 'user'
	user_id = db.Column(db.Integer, primary_key=True)
	user_name = db.Column(db.String(100))
	user_surname = db.Column(db.String(100))
	user_middle_name = db.Column(db.String(100))
	user_postal_address = db.Column(db.String(100))
	user_national_id_number = db.Column(db.String(100), unique=True)
	user_password_hash = db.Column(db.String(100))
	user_phone_number = db.Column(db.String(10))
	password_recovered = db.Column(db.Boolean, default=False)
	user_email = db.Column(db.String(100))
	created_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
	announcements = db.relationship('Announcement', backref='announcer', lazy='dynamic')
	
	"""
	def __init__(self,name="",surname="",national_id="",password="man",phone_number="",email=""):
		self.user_name = name
		self.user_surname = surname
		self.user_national_id_number = national_id
		self.user_phone_number = phone_number
		self.user_password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
		self.user_email = email
	"""
		
	def __repr__(self):
		return '<Announcer id: %s>' % self.user_national_id_number
		

class Media(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	media_name = db.Column(db.String(100))
	media_type = db.Column(db.String(100))
	media_email = db.Column(db.String(100))
	media_password = db.Column(db.String(100))
	email_confirmation = db.Column(db.Boolean, default=False)
	media = db.relationship('Announcement', backref='media_house', lazy='dynamic')
	media_print_charge = db.relationship('PrintMediaAnnouncementCharge', backref='media_print_charge', lazy='dynamic')
	media_radio_charge = db.relationship('RadioMediaAnnouncementCharge', backref='media_radio_charge', lazy='dynamic')
	announcement_type = db.relationship('AnnouncementType', backref='announcement_type', lazy='dynamic')
	
	def __repr__(self):
		return '<Media Name: %s>' % self.media_name
		
	def is_active(self):
		return self.email_confirmation
	

class AnnouncementType(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	type_name = db.Column(db.String(100))
	media_id = db.Column(db.Integer, db.ForeignKey('media.id'))
	
	
	"""
		Tells flask-login if the user account is active
	"""
	
"""	
@login_manager.user_loader
def load_user(media_id):
	return Media.get(media_id)
"""	

class Announcement(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	announcement_type = db.Column(db.String(50))
	start_day = db.Column(db.DateTime)
	end_day = db.Column(db.DateTime)
	no_of_days = db.Column(db.Integer)
	user_id =  db.Column(db.Integer, db.ForeignKey("user.user_id"))
	media_id =  db.Column(db.Integer, db.ForeignKey("media.id"))
	paid = db.Column(db.Boolean)
	charge = db.Column(db.Float)
	announced = db.Column(db.Boolean)
	print_media_announcement = db.relationship('PrintMediaAnnouncement',backref='print_media_announcement',lazy='dynamic')
	radio_media_announcement = db.relationship('RadioMediaAnnouncement',backref='radio_media_announcement',lazy='dynamic')
	radio_media_funeral_announcement = db.relationship('RadioMediaAnncouncemntFuneral',backref='radio_media_funeral_announcement',lazy='dynamic')
	
	
	
class PrintMediaAnnouncement(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	number_of_days = db.Column(db.Integer)
	picture = db.Column(db.String(50))
	content = db.Column(db.String(50))
	section = db.Column(db.String(50))
	contact = db.Column(db.Integer)
	word_count = db.Column(db.Integer)
	announcement_id =  db.Column(db.Integer, db.ForeignKey("announcement.id"))
	
class PrintMediaAnnouncementCharge(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	media_id = db.Column(db.Integer, db.ForeignKey("media.id"))
	charge_per_word = db.Column(db.Float)
	charge_per_day =  db.Column(db.Float)
	per_pic =  db.Column(db.Float)
	
	
class RadioMediaAnnouncementCharge(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	#time_slot  = db.Column(db.Integer)
	media_id = db.Column(db.Integer, db.ForeignKey("media.id"))
	charge_per_time_slot = db.Column(db.Float)
	#charge_per_day = db.Column(db.Float)
	
class RadioMediaAnnouncementTimeSlot(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	radio_media_announcement_id = db.Column(db.Integer, db.ForeignKey("radiomediaannouncement.id"))
	time_slot = db.Column(db.String(100))
	read = db.Column(db.Boolean, default=False)
	
class RadioMediaAnnouncement(db.Model):
	__tablename__ = "radiomediaannouncement"
	id = db.Column(db.Integer, primary_key=True)
	contact = db.Column(db.Integer)
	type = db.Column(db.String(50))
	no_of_time_slots = db.Column(db.Integer)
	content = db.Column(db.String(500))
	media_id = db.Column(db.Integer, db.ForeignKey("media.id"))
	announcement_id =  db.Column(db.Integer, db.ForeignKey("announcement.id"))
	radio_media_announcement_time_slot = db.relationship('RadioMediaAnnouncementTimeSlot',backref='radio_media_announcement_time_slot',lazy='dynamic')
	

	
class RadioMediaAnncouncemntFuneral(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	announcement_id =  db.Column(db.Integer, db.ForeignKey("announcement.id"))
	deceased_name = db.Column(db.String(50))
	deceased_other_name = db.Column(db.String(50))
	funeral_date = db.Column(db.DateTime, default=datetime.datetime.now)
	funeral_venue = db.Column(db.String(50))
	vigil_venue = db.Column(db.String(50))
	
	
	
	

db.create_all()

login_manager.login_view = "account_print.sign_in_view"
login_manager.login_message = u"Bonvolu ensaluti por uzi tiun paˆgon."

@login_manager.user_loader
def load_user(media_id):
	return Media.query.get(int(media_id))