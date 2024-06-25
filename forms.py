from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class VehicleForm(FlaskForm):
    name = StringField('Vehicle Name', validators=[DataRequired()])
    make = StringField('Make', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    submit = SubmitField('Add Vehicle')

class ModificationForm(FlaskForm):
    modification = StringField('Modification', validators=[DataRequired()])
    status = SelectField('Status', choices=[('Planned', 'Planned'), ('Purchased', 'Purchased')])
    submit = SubmitField('Add Modification')
