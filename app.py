from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'chickenzarecool21837'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['UPLOAD_FOLDER'] = '/static'
debug = DebugToolbarExtension(app)
app.app_context().push()
connect_db(app)
db.create_all()

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def showHomePage():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)


# @app.route('/add', methods=['POST','GET'])
# def handleAddPetForm():
#     form = AddPetForm()
#     if form.validate_on_submit():
#         data = {k:v for k,v in form.data.items() if k != "csrf_token"}
#         pet = Pet(**data)
#         db.session.add(pet)
#         db.session.commit()
#         flash('Pet has been added!',category="success")

#         return redirect('/')

#     else:
#         return render_template('pet_form.html',form=form)


# @app.route('/<int:id>', methods=['GET', 'POST'])
# def editForm(id):
#     pet = Pet.query.get_or_404(id)

#     # Dynamically remove fields from the form for editForm route
#     form = EditPetForm(obj=pet)
#     form.name = None
#     form.species = None

#     if form.validate_on_submit():
#         pet.photoUrl = form.photoUrl.data
#         pet.notes = form.notes.data
#         pet.available = form.available.data
#         db.session.commit()
#         flash('Pet has been updated!', category='success')

#         return redirect('/')

#     return render_template('edit_form.html', pet=pet, form=form)

@app.route('/add', methods=['POST', 'GET'])
def handleAddPetForm():
    form = AddPetForm()

    if form.validate_on_submit():
        photo_filename = None
        if form.photo.data:
            photo = form.photo.data
            if photo and allowed_file(photo.filename):
                filename = secure_filename(photo.filename)
                quit()photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                photo_filename = filename

        pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photoUrl=form.photoUrl.data if form.photoUrl.data else None,
            photo_filename=photo_filename,
            age=form.age.data,
            notes=form.notes.data,
            available=form.available.data
        )
        db.session.add(pet)
        db.session.commit()
        flash('Pet has been added!', category="success")

        return redirect('/')

    return render_template('pet_form.html', form=form)


@app.route('/<int:id>', methods=['GET', 'POST'])
def editForm(id):
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        photo_filename = None
        if form.photo.data:
            photo = form.photo.data
            if photo and allowed_file(photo.filename):
                filename = secure_filename(photo.filename)
                photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                photo_filename = filename

        pet.photoUrl = form.photoUrl.data if form.photoUrl.data else None
        pet.photo_filename = photo_filename
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash('Pet has been updated!', category='success')

        return redirect('/')

    return render_template('edit_form.html', pet=pet, form=form)