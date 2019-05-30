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
    title = StringField('Pitch title',validators=[Required()])
    category_id = SelectField("Select Category :", choices=[('c', 'select'), (
        '1', 'Educational'), ('2', 'Agricultural'), ('3', 'Sports'), ('4', 'Science'), ('5', 'Technology')])
    pitch = TextAreaField(" Post your pitch", validators=[Required()])
    submit = SubmitField("Add your pitch ")


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    '''
    Class to create a wtf form for creating a pitch
    '''
    feedback = TextAreaField('WRITE COMMENT',validators=[Required()])
    submit = SubmitField('SUBMIT')

class CategoryForm(FlaskForm):
    '''
    Class to create a wtf form for creating a pitch
    '''
    category_id = SelectField("Select Category :", choices=[('c', 'select'), (
        '1', 'Health Related'), ('2', 'Robotics'), ('3', 'Manufacturing'), ('4', 'IoT'), ('5', 'Life inspiring')])
    pitch = TextAreaField(" Post your pitch", validators=[Required()])
    submit = SubmitField("Add Pitch ")
