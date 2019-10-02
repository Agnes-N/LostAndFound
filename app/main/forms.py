from flask_wtf import  FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField,FileField,IntegerField
from wtforms.validators import Required
from flask_wtf.file import FileField, FileRequired
# from ..models import Lost

class LostForm(FlaskForm):

    name = StringField('Enter your name(Names on your documents)', validators=[Required()])
    address = StringField('Place of Issue', validators=[Required()])
    category = SelectField('Category',choices=[('National_ID','National_ID'),('Passport','Passport'),('degree','degree')], validators=[Required()])
    location = StringField('Your Location', validators=[Required()])
    phone = IntegerField('Your Tel', validators=[Required()])
    description = TextAreaField('Write a brief description on what you have lost', validators=[Required()])
    
    submit = SubmitField('submit')

class UpdateLostForm(FlaskForm):

    name = StringField('Enter your name(Names on your documents)', validators=[Required()])
    address = StringField('Place of Issue', validators=[Required()])
    category = SelectField('Category',choices=[('National_ID','National_ID'),('Passport','Passport'),('degree','degree')], validators=[Required()])
    location = StringField('Your Location', validators=[Required()])
    phone = IntegerField('Your Tel', validators=[Required()])
    
    submit = SubmitField('submit')

class FoundForm(FlaskForm):

    name = StringField('Names on documents', validators=[Required()])
    category = SelectField('Category',choices=[('National_ID','National_ID'),('Passport','Passport'),('degree','degree')], validators=[Required()])
    address = StringField('Place of Issue', validators=[Required()])
    image = FileField('Photo', validators=[FileRequired()])
    
    submit = SubmitField('submit')