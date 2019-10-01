from flask_wtf import  FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField
from wtforms.validators import Required
# from ..models import Lost

class LostForm(FlaskForm):

    name = StringField('Name', validators=[Required()])
    category = SelectField('Category',choices=[('National_ID','National_ID'),('Passport','Passport'),('degree','degree')], validators=[Required()])
    address = TextAreaField('Your address', validators=[Required()])
    
    submit = SubmitField('Pitch')