from flask import render_template,request,redirect,flash,url_for,abort
from . import main
# from flask_login import login_user,login_required,current_user
from ..models import User
from .. import db,photos
# from .forms import BlogForm,CommentForm,UpdateBlogForm,SubscriptionForm,UpdateProfile


@main.route('/', methods=['GET','POST'])
def index():


    return render_template('index.html')