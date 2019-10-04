from flask_wtf import  FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField,FileField,IntegerField
from wtforms.validators import Required,DataRequired

# ''''
# https://stackoverflow.com/questions/49633323/wtforms-date-validation
# ''''
from flask_wtf.file import FileField, FileRequired
from datetime import date
from wtforms.fields.html5 import DateField,DateTimeField

class LostForm(FlaskForm):

    name = StringField('Enter your name(Names on your documents)', validators=[Required()])
    address = StringField('Place of Issue', validators=[Required()])
    category = SelectField('Category',choices=[('National_ID','National_ID'),('Passport','Passport'),('degree','degree')], validators=[Required()])
    location = StringField('Your Location', validators=[Required()])
    phone = IntegerField('Your Tel', validators=[Required()])
    description = TextAreaField('Write a brief description on what you have lost', validators=[Required()])
    posted_date = DateField("Posted Date", validators=[DataRequired(message="You need to enter the posted date.")], format='%Y-%m-%d')
    
    submit = SubmitField('submit')

class UpdateLostForm(FlaskForm):

    name = StringField('Enter your name(Names on your documents)', validators=[Required()])
    address = StringField('Place of Issue', validators=[Required()])
    category = SelectField('Category',choices=[('National_ID','National_ID'),('Passport','Passport'),('degree','degree')], validators=[Required()])
    location = StringField('Your Location', validators=[Required()])
    phone = IntegerField('Your Tel', validators=[Required()])
    posted_date = DateField("Posted Date", validators=[DataRequired(message="You need to enter the posted date.")], format='%Y-%m-%d')
    
    submit = SubmitField('submit')

class FoundForm(FlaskForm):

    name = StringField('Names on documents', validators=[Required()])
    f_name = StringField('Names of Discoverer', validators=[Required()])
    address = StringField('Place of Issue', validators=[Required()])
    category = SelectField('Category',choices=[('National_ID','National_ID'),('Passport','Passport'),('degree','degree')], validators=[Required()])
    location = StringField('Discoverer Location', validators=[Required()])
    phone = IntegerField('Discoverer Tel', validators=[Required()])
    description = TextAreaField('Write a brief description', validators=[Required()])
    image = FileField('Photo', validators=[FileRequired()])
    posted_date = DateField("Posted Date", validators=[DataRequired(message="You need to enter the posted date.")], format='%Y-%m-%d')
    
    submit = SubmitField('submit')

class UpdateFoundForm(FlaskForm):

    name = StringField('Names on documents', validators=[Required()])
    f_name = StringField('Names of Discoverer', validators=[Required()])
    address = StringField('Place of Issue', validators=[Required()])
    category = SelectField('Category',choices=[('National_ID','National_ID'),('Passport','Passport'),('degree','degree')], validators=[Required()])
    location = StringField('Discoverer Location', validators=[Required()])
    phone = IntegerField('Discoverer Tel', validators=[Required()])
    description = TextAreaField('Write a brief description', validators=[Required()])
    image = FileField('Photo', validators=[FileRequired()])
    posted_date = DateField("Posted Date", validators=[DataRequired(message="You need to enter the posted date.")], format='%Y-%m-%d')
    
    submit = SubmitField('submit')