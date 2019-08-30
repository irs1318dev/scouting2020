from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired

# this is the form page, which allows for user input

class MatchForm(FlaskForm):
    name_number = IntegerField('Number of people',
                        validators=[DataRequired()])
    match_number = IntegerField('Amount of Matches',
                        validators=[DataRequired()])
    match_row = IntegerField('Number of matches per row',
                        validators=[DataRequired()])
    robot_number = IntegerField('How many Robots are being scouted', validators=[DataRequired()])
    submit = SubmitField('Next Step')

class Match2Form(FlaskForm):
    name_list = StringField('List the names of people seperated by commas. EX: "jeff, stutler, mason m., sarah, etc."', validators=[DataRequired()])
    submit = SubmitField('Next Step')

class TimeForm(FlaskForm):
    name_number = IntegerField('Number of people',
                        validators=[DataRequired()])
    time_number1 = IntegerField('Time range from start to lunch',
                        validators=[DataRequired()])
    time_number2 = IntegerField('Time range from lunch to end',
                        validators=[DataRequired()])
    time_row = IntegerField('Number of matches per row',
                        validators=[DataRequired()])
    robot_number = IntegerField('How many Robots are being scouted', validators=[DataRequired()])
    submit = SubmitField('Next Step')