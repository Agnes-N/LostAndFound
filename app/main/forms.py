from flask_wtf import  FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField,FileField
from wtforms.validators import Required
from flask_wtf.file import FileField, FileRequired
# from ..models import Lost

class LostForm(FlaskForm):

    name = StringField('Enter your name(Names on your documents)', validators=[Required()])
    address = StringField('Place of Issue', validators=[Required()])
    category = SelectField('Category',choices=[('National_ID','National_ID'),('Passport','Passport'),('degree','degree')], validators=[Required()])
    """
    https://stackoverflow.com/questions/50168932/how-to-upload-an-image-using-wtf-forms-quick-form
    """
    image = FileField(validators=[FileRequired()])
    
    submit = SubmitField('submit')

class FoundForm(FlaskForm):

    name = StringField('Name', validators=[Required()])
    category = SelectField('Category',choices=[('National_ID','National_ID'),('Passport','Passport'),('degree','degree')], validators=[Required()])
    address = TextAreaField('Your address', validators=[Required()])
    image = FileField('Photos)
    
    submit = SubmitField('submit')