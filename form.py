from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, DataRequired



class InputFieldForm(FlaskForm):

	def my_length_check(form, field):
		if not 0 < len(field.data) <= 20:
			raise ValidationError('Field must be between 1 and 20 characters')


	VALUES = ("",100, 200,300,400,500,600,800,1000)
	values_to_show = (10,25,50,100,200)
	searchword = StringField("Search by Keyword", [InputRequired()])
	date = DateField("Start", format='%Y/%m/%d')
	date2 = DateField("End", format='%Y/%m/%d')
	category_ID = IntegerField("Category ID")
	difficulty = SelectField('Difficulty', choices=[(value, value) for value in VALUES], default= (None,None))
	submit = SubmitField("Search!")
	show_count = SelectField('Number of Values to Show', choices=[(value, value) for value in values_to_show], default= (25,25))


	
	

class Randomizer(FlaskForm):
	submit = SubmitField("Surprise Me")


