from flask import render_template,request,redirect,flash,url_for,abort
from . import main
# from flask_login import login_user,login_required,current_user
from flask_login import current_user
from ..models import User,Lost
from .. import db,photos
from .forms import LostForm



@main.route('/', methods=['GET','POST'])
def index():

    title = 'Welcome to Lost and Found website'
        # return redirect(url_for('main.index')
    return render_template('index.html', title = title)

@main.route('/lost', methods=['GET','POST'])
def lost():

    losts = Lost.query.all()

    return render_template('declare_lost.html',losts = losts)

@main.route('/declare_lost', methods=['GET','POST'])
def declare_lost():

    form = LostForm()
    if form.validate_on_submit():

        category = form.category.data
        address = form.address.data
        name = form.name.data
        # user_id = current_user
        # user_id = current_user._get_current_object().id,

        new_lost_object = Lost(category = category,address = address, name = name)
        new_lost_object.save_lost()

        return redirect(url_for('main.lost'))

    return render_template('declare_lost.html',form = form)