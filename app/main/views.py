from flask import render_template,request,redirect,flash,url_for,abort
from . import main
# from flask_login import login_user,login_required,current_user
from flask_login import current_user
from ..models import User,Lost,Found
from .. import db,photos
from .forms import LostForm,FoundForm
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
        location = form.location.data
        phone = form.phone.data

        image = form.image.data
        filename = photos.save(image)

        path = f'photos/{filename}'
        new_lost_object = Lost(category = category,address = address, name = name,image = path,location = location,phone = phone)
        new_lost_object.save_lost()

        return redirect(url_for('main.lost'))

    return render_template('declare_lost.html',form = form)

@main.route('/lost/<int:id>/delete', methods = ['GET','POST'])
# @login_required
def delete(id):
    current_post = Lost.query.filter_by(id = id).first()

    # if current_post.user != current_user:
    #     abort(404)
    db.session.delete(current_post)
    db.session.commit()
    return redirect(url_for('.lost'))

@main.route('/found', methods=['GET','POST'])
def found():

    founds = Found.query.all()

    return render_template('found.html',founds = founds)

@main.route('/declare_found', methods=['GET','POST'])
def declare_found():

    forme = FoundForm()

    if forme.validate_on_submit():

        category = forme.category.data
        address = forme.address.data
        name = forme.name.data
        image = forme.image.data

        filename = photos.save(image)
        print(filename)
        path = f'photos/{filename}'

        new_found_object = Found(category = category,address = address, name = name , image = path)
        new_found_object.save_found()

        return redirect(url_for('main.found'))

    return render_template('declare_found.html',forme = forme)
