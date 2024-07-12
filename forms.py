from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField, SelectField, IntegerField
from wtforms.validators import DataRequired

class BMIForm(FlaskForm):
    weight = FloatField('Weight', validators=[DataRequired()])
    height = FloatField('Height', validators=[DataRequired()])
    unit = SelectField('Unit', choices=[('metric', 'Metric (kg, cm)'), ('imperial', 'Imperial (lbs, inches)')])
    submit = SubmitField('Calculate BMI')

class BMRForm(FlaskForm):
    weight = FloatField('Weight', validators=[DataRequired()])
    height = FloatField('Height', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired()])
    unit = SelectField('Unit', choices=[('metric', 'Metric (kg, cm)'), ('imperial', 'Imperial (lbs, inches)')])
    submit = SubmitField('Calculate BMR')
