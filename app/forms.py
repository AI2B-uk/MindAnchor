from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class JournalForm(FlaskForm):
    content = TextAreaField('Write your thoughts', validators=[DataRequired()])
    submit = SubmitField('Save Entry')

class SettingsForm(FlaskForm):
    notifications = SelectField('Notification Preferences', choices=[('all', 'Receive all notifications'), ('essential', 'Only essential notifications'), ('none', 'No notifications')])
    theme = SelectField('Theme', choices=[('light', 'Light'), ('dark', 'Dark')])
    submit = SubmitField('Save Settings')
