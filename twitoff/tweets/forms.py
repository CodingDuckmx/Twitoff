from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SearchTwitterUser(FlaskForm):
    twname = StringField('Username', default='Twitter', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Sumbit')