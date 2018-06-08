from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SelectField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo

from flaskr.models import User


highlighters = [
    ('no-highlight', 'RAW'),
    ('xml', 'HTML / XML'),
    ('css', 'CSS'),
    ('js', 'Javascript / JSON'),
    ('markdown', 'Markdown'),
    ('python', 'Python'),
    ('go', 'Golang')
]


class LoginForm(FlaskForm):
    username = StringField('USERNAME', validators=[DataRequired()])
    password = PasswordField('PASSWORD', validators=[DataRequired()])
    remember_me = BooleanField('REMEMBER ME')
    submit = SubmitField('LOGIN')


class RegistrationForm(FlaskForm):
    username = StringField('USERNAME', validators=[DataRequired()])
    password = PasswordField('PASSWORD', validators=[DataRequired()])
    confirm = PasswordField(
        'CONFIRM PASSWORD', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('REGISTER')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username invalid.')


class TrashForm(FlaskForm):
    title = StringField("TITLE", validators=[DataRequired()])
    content = TextAreaField("CONTENT", render_kw={"rows": 10}, validators=[DataRequired()])
    highlight = SelectField("HIGHLIGHT", choices=highlighters, validators=[DataRequired()])
    password = PasswordField('PASSWORD (optional)', default='')
    visibility = SelectField("VISIBILITY", choices=[('private','Private'),('public', 'Public')], validators=[DataRequired()])
    submit = SubmitField("CREATE")
