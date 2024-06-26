from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField  # Add SelectField here
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already in use.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class VehicleForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    make = StringField('Make', validators=[DataRequired(), Length(min=2, max=100)])
    model = StringField('Model', validators=[DataRequired(), Length(min=2, max=100)])
    year = IntegerField('Year', validators=[DataRequired(), NumberRange(min=1886, max=2024)])
    submit = SubmitField('Add Vehicle')

class AddModificationForm(FlaskForm):
    modification = StringField('Modification', validators=[DataRequired(), Length(min=2, max=100)])
    status = SelectField('Status', choices=[('Planned', 'Planned'), ('Purchased', 'Purchased'), ('Installed', 'Installed')], validators=[DataRequired()])
    submit = SubmitField('Add Modification')




