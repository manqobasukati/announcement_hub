#forms 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField, PasswordField, FloatField
from wtforms.validators import DataRequired, EqualTo

class MediaSignUpForm(FlaskForm):

	media_house_types = [
							('print_media','Print Media'),
							('radio_media','Radio Media')
						]
						
	media_name = StringField('Media House',validators=[DataRequired()])
	media_email = StringField('Email address',validators=[DataRequired()])
	media_type = SelectField('Media Type',choices=media_house_types)
	media_password = PasswordField('Password',validators=[DataRequired(),EqualTo('confirm',message='Passwords must match')])
	confirm = PasswordField('Repeat Password')
	submit = SubmitField('Sign up')
	
	
class MediaSignInForm(FlaskForm):
	media_email = StringField('Email address',validators=[DataRequired()])
	media_password = PasswordField('Password',validators=[DataRequired()])
	submit = SubmitField('Sign in')
	
class AnnouncementCriteriaPrint(FlaskForm):
	
	announced = SelectField('Announced' , choices=[('1','Yes'),('0','No')])
	submit = SubmitField('submit')
	
class AnnouncementCriteriaRadio(FlaskForm):
	time_slot = SelectField('Time Slot',choices=[('1','Morning'),('2','Afternoon')])
	announced = SelectField('Announced' , choices=[('1','Yes'),('0','No')])
	submit = SubmitField('submit')
	
	
class RadioSetRatesForm(FlaskForm):
	charge_per_slot = FloatField('Charge per slot')
	submit = SubmitField('submit')
	

	
class PrintSetRatesForm(FlaskForm):
	charge_per_word = FloatField('Charge per word')
	charge_per_pic = FloatField('Charge per pic')
	charge_per_day = FloatField('Charge per day')
	submit = SubmitField('submit')
		
	