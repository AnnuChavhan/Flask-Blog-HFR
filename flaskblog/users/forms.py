from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField,ValidationError,BooleanField
from wtforms.validators import DataRequired,Length,EqualTo,Email
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username= StringField('Username',validators=[DataRequired(),Length(min=2,max=10)])
    email=StringField('Email',validators=[Email(), DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm_Password',validators=[DataRequired(),EqualTo('password')])
    submit =SubmitField('SignUp')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This User Name Is Already Taken')

    def validate_email(self,email):
        user_email= User.query.filter_by(email=email.data).first()
        if user_email:
            raise ValidationError('This Email Id Is Already Taken')


class LoginForm(FlaskForm):
    email=StringField('Email',validators=[Email(),DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit= SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=10)])
    email=StringField('Email', validators=[DataRequired(),Email()])
    picture= FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png','jpeg'])])
    submit =SubmitField('Update')

    def vlidate_username(self,username):
        if username.data != current_user.username:
            user= User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That UserName Already Taken Please Choose A different UserName')

    def vidate_email(self,email):
        if email != current_user.email:
            user= User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That Email Is Taken.Please Choose a Different Email')

class ResetRequestTokenForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Reset Password')

    def validate_email(self,email):
        user_mail=User.query.filter_by(email=email.data).first()
        if user_mail is None:
            raise ValidationError('Please Provide valid email Address....Register to Login')

class ResetPasswordTokenForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm_Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
