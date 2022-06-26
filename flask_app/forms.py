from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.fields import FloatField, IntegerField

class MaterialsForm(FlaskForm):
    SO2 = FloatField('오염수치', validators=[DataRequired('오염수치')])
    NO2 = FloatField('오염수치', validators=[DataRequired('오염수치')])
    CO = FloatField('오염수치', validators=[DataRequired('오염수치')])
    O3 = IntegerField('오염수치', validators=[DataRequired('오염수치')])
    PM10 = IntegerField('오염수치', validators=[DataRequired('오염수치')])
    PM2_5 = IntegerField('오염수치', validators=[DataRequired('오염수치')])



