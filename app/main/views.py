from flask import render_template,request,redirect,flash,url_for,abort
from . import main
# from flask_login import login_user,login_required,current_user
from flask_login import current_user
from ..models import User,Lost
from .. import db,photos
from .forms import LostForm
from werkzeug.utils import secure_filename

@main.route('/', methods=['GET','POST'])
def index():

    title = 'Lost and Found'
    return render_template('index.html', title = title)

@main.route('/lost', methods=['GET','POST'])
def lost():

    losts = Lost.query.all()

    return render_template('lost.html',losts = losts)

@main.route('/declare_lost', methods=['GET','POST'])
def declare_lost():

    form = LostForm()
    if form.validate_on_submit():

        name = form.name.data  
        address = form.address.data
        category = form.category.data
        image = form.image.data
        filename = photos.save(image)
        print(filename)
        path = f'photos/{filename}'
        new_lost_object = Lost(category = category,address = address, name = name,image = path)
        new_lost_object.save_lost()

        return redirect(url_for('main.lost'))

    return render_template('declare_lost.html',form = form)

@main.route('/found', methods=['GET','POST'])
def found():

    founds = Found.query.all()

    return render_template('found.html',founds = founds)

@main.route('/declare_found', methods=['GET','POST'])
def declare_found():

    form = FoundForm()
    if form.validate_on_submit():

        category = form.category.data
        address = form.address.data
        name = form.name.data
        image = form.name.data

        new_found_object = Found(category = category,address = address, name = name , image = image)
        new_found_object.save_found()

        return redirect(url_for('main.found'))

    return render_template('declare_found.html',form = form)
