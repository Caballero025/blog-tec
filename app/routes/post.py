from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Post
from app.models import Category

posts_bp = Blueprint ('posts',__name__)



@posts_bp.route('/')
def listar_posts():
    posts = Post.query.all()
    categories = Category.query.all()
    return render_template('posts/listar_posts.html', posts=posts, categories=categories)
#Crear post
@posts_bp.route('/new',methods=['GET','POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category_id = request.form.get('category_id')
        new_post = Post(title=title, content=content, category_id=category_id)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('posts.listar_posts'))
    
    #Aqui sigue si es GET
    categories = Category.query.all()
    return render_template('posts/create_post.html', categories=categories)
#Actualizar post
@posts_bp.route('/update/<int:id>', methods=['GET','POST'])
def update_post(id):
    post = Post.query.get(id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.category_id = request.form['category_id']
        post.content = request.form['content']
        db.session.commit()
        return redirect(url_for('posts.listar_posts'))
    
    categories = Category.query.all()
    return render_template('posts/update_post.html', post=post, categories=categories)

#Eliminar post
@posts_bp.route('/delete/<int:id>')
def delete_post(id):
    post = Post.query.get(id)
    if post:
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('posts.listar_posts'))

