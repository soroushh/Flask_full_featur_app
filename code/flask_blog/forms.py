from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_blog.models import User

class RegistrationForm(FlaskForm):
    username = StringField("username",
                           validators=[DataRequired(),
                                       Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(),
                                             Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("The username is already taken, Please define another one.")

    def validate_email(self, email):
        user_by_email = User.query.filter_by(email=email.data).first()
        if user_by_email:
            raise ValidationError("The email is defined for another user. Choose a different one please.")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Log in")
