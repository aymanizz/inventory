from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class CreateOrUpdateItemForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=120)])
    description = StringField("Description", validators=[Length(max=200)])
    quantity = IntegerField(
        "quanitty", validators=[DataRequired(), NumberRange(min=0, max=10)]
    )
    unit = StringField("Unit", validators=[DataRequired(), Length(max=10)])
    submit = SubmitField("Submit")


class DeleteItemForm(FlaskForm):
    comment = StringField("Comment", validators=[Length(max=200)])
    submit = SubmitField("Delete")


class ActionForm(FlaskForm):
    submit = SubmitField("Submit")
