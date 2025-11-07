from flask import Flask, render_template, request, redirect, url_for
import os
import json

app = Flask(__name__)

def load_posts():
    """
    Load blog posts from the JSON storage file located in the static folder.

    Returns:
        list: A list of dictionaries, each representing a blog post.
    """
    json_path = os.path.join(app.static_folder, 'blog_posts.json')
    with open(json_path, 'r') as f:
        return json.load(f)

def save_posts(posts):
    """
    Save the updated list of blog posts back to the JSON storage file.

    Args:
        posts (list): A list of dictionaries representing blog posts to save.
    """
    json_path = os.path.join(app.static_folder, 'blog_posts.json')
    with open(json_path, 'w') as f:
        json.dump(posts, f, indent=4)


@app.route('/')
def index():
    """
    Index route that displays all blog posts.

    Retrieves blog posts from storage and renders the 'index.html' template
    with the list of posts.

    Returns:
        Response: Rendered HTML page showing all blog posts.
    """
    posts = load_posts()
    return render_template('index.html', posts=posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Route to add a new blog post.

    GET: Renders the 'add.html' form for creating a new post.
    POST: Processes the form submission, creates a new blog post with a unique ID,
          saves it, and redirects to the index page.

    Returns:
        Response: Form page for GET, redirect response for POST.
    """
    if request.method == 'POST':
        posts = load_posts()

        new_id = max(post['id'] for post in posts) + 1 if posts else 1
        new_post = {
            "id": new_id,
            "author": request.form.get('author'),
            "title": request.form.get('title'),
            "content": request.form.get('content')
        }

        posts.append(new_post)
        save_posts(posts)

        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/delete/<int:post_id>')
def delete(post_id):
    """
    Route to delete a blog post by its ID.

    Args:
        post_id (int): The unique identifier of the post to delete.

    Returns:
        Response: Redirects to the index page after deletion.
    """
    posts = load_posts()
    posts = [post for post in posts if post['id'] != post_id]
    save_posts(posts)
    return redirect(url_for('index'))

@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """
    Route to update an existing blog post.

    GET: Renders the 'update.html' form pre-populated with current post data.
    POST: Processes the form submission to update the post data and saves the changes.

    Args:
        post_id (int): The unique identifier of the post to update.

    Returns:
        Response: Pre-populated form for GET, redirect after update for POST.
    """
    posts = load_posts()
    post = next((p for p in posts if p['id'] == post_id), None)
    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        post['author'] = request.form.get('author')
        post['title'] = request.form.get('title')
        post['content'] = request.form.get('content')
        save_posts(posts)
        return redirect(url_for('index'))

    # GET request: render the update form pre-filled with post's current data
    return render_template('update.html', post=post)

@app.route('/like/<int:post_id>')
def like(post_id):
    """
    Route to increment the like count of a blog post.

    Args:
        post_id (int): The unique identifier of the post to like.

    Returns:
        Response: Redirects to the index page after incrementing likes.
    """
    posts = load_posts()
    for post in posts:
        if post['id'] == post_id:
            post['likes'] = post.get('likes', 0) + 1
            break
    save_posts(posts)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)