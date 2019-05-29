from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import Required


class ReviewForm(FlaskForm):
    title = StringField('Review title', validators=[Required()])
    review = TextAreaField('Pitch review')
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    '''
    Class to create a wtf form for creating a pitch
    '''
    category_id = SelectField("Select Category :", choices=[('c', 'select'), (
        '1', 'Artifitial Intelegence'), ('2', 'Robotics'), ('3', 'Drones'), ('4', 'IoT'), ('5', 'Data Science')])
    pitch = TextAreaField(" Post your pitch", validators=[Required()])
    submit = SubmitField("Add your pitch ")


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    '''
    Class to create a wtf form for creating a pitch
    '''
    feedback = TextAreaField('WRITE COMMENT')
    submit = SubmitField('SUBMIT')


class DisplayPitch(FlaskForm):
    text = TextAreaField('Write your pitch', validators=[Required()])
    categories = SelectField('Select Category', choices=[('EDUCATIONAL', 'EDUCATIONAL'), (
        'BUSINESS', 'BUSINESS'), ('TECHNOLOGY','TECHNOLOGY'),('INSPIRATIONAL', 'INSPIRATIONAL'), ('SPORTS', 'SPORTS')])
    submit = SubmitField('post')


class CategoryForm(FlaskForm):
    '''
    Class to create a wtf form for creating a pitch
    '''
    category_id = SelectField("Select Category :", choices=[('c', 'select'), (
        '1', 'Health Related'), ('2', 'Robotics'), ('3', 'Manufacturing'), ('4', 'IoT'), ('5', 'Life inspiring')])
    pitch = TextAreaField(" Post your pitch", validators=[Required()])
    submit = SubmitField("Add Pitch ")
