#admin page
from app import *
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import db
from models import User, Media, Announcement, AnnouncementType,PrintMediaAnnouncement, PrintMediaAnnouncementCharge, RadioMediaAnnouncement,RadioMediaAnncouncemntFuneral,RadioMediaAnnouncementCharge





#admin = Admin(app,'Hub admin')
class AnnouncementView(ModelView):
	column_display_pk = True
	#column_include_list=['PrintMediaAnnouncement.id',]
	#column_display_all_relations = True
	column_editable_list = ['announcement_type','user_id']
	
class MediaView(ModelView):
	column_display_pk = True
	
class UserView(ModelView):
	column_display_pk = True
	
class RadioMediaView(ModelView):
	column_display_pk = True
	
class RadioFuneralMediaView(ModelView):
	column_display_pk = True

admin.add_view(UserView(User, db.session))
admin.add_view(MediaView(Media, db.session))
admin.add_view(AnnouncementView(Announcement,db.session))
admin.add_view(ModelView(PrintMediaAnnouncement, db.session))
admin.add_view(ModelView(PrintMediaAnnouncementCharge, db.session))
admin.add_view(RadioMediaView(RadioMediaAnnouncement, db.session))
admin.add_view(RadioFuneralMediaView(RadioMediaAnncouncemntFuneral,db.session))
admin.add_view(ModelView(RadioMediaAnnouncementCharge, db.session))
admin.add_view(ModelView(AnnouncementType,db.session))











