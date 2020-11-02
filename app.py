#IMPORTS
from flask import Flask, render_template, request, redirect
import pymongo
from models import PostModel

# DATABASE
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://khal:onaolapo16.@cluster0.ibqpf.gcp.mongodb.net/mydb?retryWrites=true&w=majority"
mongo = PyMongo(app)

#URLS MAPPING
@app.route('/')
def post_list():
    all_posts=PostModel().get_posts()
    # pprint(all_posts)
    # all_posts = Post.query.order_by(-Post.created_date).all()
    return render_template("home.html", posts=all_posts)

    @app.route('/new_post', methods = ['GET', 'POST'])
    def posts():
        if request.method == 'POST':
            post_title = request.form['title']
            post_content = request.form['content']
            post_author = request.form['author']

            all_posts=PostModel(author=post_author, content=post_content, title=post_title).save()
        return redirect('/')
    else:
        return render_template("new_post.html")

@app.route('/posts/delete/<id>')
def delete(id):
    post = PostModel().delete_post(id)

    return redirect('/')


@app.route('/posts/edit/<id>', methods = ['GET','POST'])
def edit(id):
    post = PostModel().get_post(id)

    if request.method == 'POST':
        if post:
            title = request.form['title']
            content = request.form['content']
            author = request.form['author']

            post = PostModel().update_post(
                id,
                {
                    "title": title,
                    "content": content,
                    "author": author
                }
            )
            return redirect('/')

        # if post with that id is invalid, return not found (404)
        return abort(404)
    else:
        return render_template("update.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
