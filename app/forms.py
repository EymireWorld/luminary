from wtforms import EmailField, Form, PasswordField, StringField
from wtforms.validators import InputRequired, Length


class RegistrationForm(Form):
    username = StringField('Username', [InputRequired(), Length(min= 4, max= 16)])
    first_name = StringField('First name', [InputRequired()])
    last_name = StringField('Last name', [InputRequired()])
    email = EmailField('Email', [InputRequired()])
    password = PasswordField('Password', [InputRequired()])


class CommentForm(Form):
    text = StringField('Comment text', [InputRequired(), Length(min= 8, max= 256)])
