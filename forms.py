from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email, Optional, AnyOf, Regexp, URL, NumberRange, ValidationError
from flask_wtf.file import FileAllowed, FileRequired, FileField


class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired(message="Pet name is required")])
    species = StringField("Species", validators=[InputRequired(message="Species is required"), AnyOf(["Dog","Cat","Porcupine","dog","cat","porcupine"], message="Only accepting: Dog, Cat, or Porcupine")])
    photo = FileField("Photo", validators=[FileAllowed(['jpg', 'jpeg', 'png'], message="Only JPG, JPEG, and PNG images are allowed."), Optional()])
    photoUrl = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30, message="Only accepting pets under 31 years of age.")])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available")

    def validate(self):
        if not super().validate():
            return False

        if not self.photo.data and not self.photoUrl.data:
            return True  # Allow both fields to be excluded

        return True


class EditPetForm(FlaskForm):
    photo = FileField("Photo", validators=[FileAllowed(['jpg', 'jpeg', 'png'], message="Only JPG, JPEG, and PNG images are allowed."), Optional()])
    photoUrl = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available")

    def validate(self):
        if not super().validate():
            return False

        if not self.photo.data and not self.photoUrl.data:
            return True  # Allow both fields to be excluded

        return True