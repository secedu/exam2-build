from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length

# Set your classes here.


class RegisterForm(FlaskForm):
    name = TextField(
        'Username', validators=[DataRequired(), Length(min=6, max=25)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        'Repeat Password',
        [DataRequired(),
        EqualTo('password', message='Passwords must match')]
    )


class LoginForm(FlaskForm):
    name = TextField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])


class ModifyForm(FlaskForm):
    firstname = TextField(
        'First Name', validators=[DataRequired(), Length(min=1, max=64)]
    )
    lastname = TextField(
        'Last Name', validators=[DataRequired(), Length(min=1, max=64)]
    )
    signature = TextField(
        'Signature'
    )

class SendMsgForm(FlaskForm):
    mailbox = TextField(
        'Mailbox Token', validators=[DataRequired(), Length(min=36, max=36)]
    )
    message = TextField(
        'Message', validators=[DataRequired(), Length(min=1, max=440)]
    )
