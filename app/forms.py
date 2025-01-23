from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    text = StringField('Mensaje', validators=[DataRequired()])
    submit = SubmitField('Enviar')
