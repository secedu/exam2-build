from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, HiddenField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('USERNAME', validators=[DataRequired()])
    password = PasswordField('PASSWORD', validators=[DataRequired()])
    role = HiddenField(DataRequired(), default='user')
    submit = SubmitField('LOGIN')


class ResetForm1(FlaskForm):
    username = StringField('USERNAME', validators=[DataRequired()])
    submit = SubmitField('SUBMIT')


class ResetForm2(FlaskForm):
    username = HiddenField('USERNAME', validators=[DataRequired()])
    response = StringField('SECRET ANSWER')
    password = PasswordField('NEW PASSWORD', validators=[DataRequired()])
    submit = SubmitField('RESET')