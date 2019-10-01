from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, ValidationError, SubmitField, ValidationError,SubmitField,BooleanField,TextAreaField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(),Email()])
    username =StringField('Enter your user name',validators=[Required()])
    password = PasswordField('password',validators= [Required(),
    EqualTo('password_confirm', message ='Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords', validators =[Required()])
    submit =SubmitField('Sign Up')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
              raise ValidationError('there is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
          raise ValidationError('That username is taken')
class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password =PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
