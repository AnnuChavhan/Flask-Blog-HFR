from flask import render_template,redirect,url_for,request,Blueprint,flash,abort
from flask_login import login_required,current_user
from flaskblog.posts.forms import PostForm
from flaskblog.models import Post,User
from flaskblog import db

posts=Blueprint('posts',__name__)

@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.hello_world'))
    return render_template('create.html',title='New Post',form=form)

@posts.route("/post/<int:id>",methods=["GET","POST"])
def post(id):
    post = Post.query.get_or_404(id)
    return render_template('post.html', post=post)

@posts.route("/post/<int:id>/update",methods=['GET','POST'])
@login_required
def update_post(id):
    post = Post.query.get_or_404(id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your Post Has Been Updated!!!','success')
        return redirect(url_for('posts.post', id=post.id))
    elif request.method =='GET':
        form.title.data= post.title
        form.content.data= post.content
    return render_template('create.html',title='Update Post',form=form)

@posts.route("/post/<int:id>/delete",methods=['POST'])
@login_required
def delete_post(id):
    post=Post.query.get_or_404(id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your Post Has Been Deleted!!','success')
    return redirect(url_for('main.hello_world'))

