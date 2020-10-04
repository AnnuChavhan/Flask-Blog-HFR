from flask import render_template,redirect,url_for,Blueprint,request
from flaskblog.models import Post

main=Blueprint('main',__name__)

@main.route('/')
@main.route('/home')
def hello_world():
    page = request.args.get('page', 1, type=int)
    posts=Post.query.paginate(page=page, per_page=2)
    return render_template('home.html' , posts = posts)

@main.route('/about')
def about():
    return render_template('about.html',title='About')
