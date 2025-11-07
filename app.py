from flask import Flask, render_template
import os
import json

app = Flask(__name__)

def load_posts():
    json_path = os.path.join(app.static_folder, 'blog_posts.json')
    with open(json_path, 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    posts = load_posts()
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)