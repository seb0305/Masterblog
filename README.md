# Flask Blog App
**Simple Full-CRUD Blog Platform: Create, Read, Update, Delete & Like Posts (JSON-Powered Backend)**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-green)](https://flask.palletsprojects.com/)
[![HTML/CSS](https://img.shields.io/badge/HTML-CSS-orange)](https://developer.mozilla.org/docs/Web/HTML)
[![JSON](https://img.shields.io/badge/JSON-Storage-yellow)](https://www.json.org/)

## 🎯 Features

| Feature | Description |
|---------|-------------|
| **Post Listing** | Homepage displays all posts with author, title, content, like count  |
| **Add New Posts** | Form-based creation with auto ID generation & immediate persistence  |
| **Edit Posts** | Pre-filled update form for any post by ID, saves changes instantly  |
| **Delete Posts** | One-click removal from list, refreshes page on success  |
| **Like System** | Increment like counter per post via dedicated endpoint  |
| **JSON Persistence** | All data stored in `static/blog_posts.json` – no database needed |

## 🏗️ Tech Stack

Frontend: Vanilla HTML forms + Jinja2 templates (`index.html`, `add.html`, `update.html`) + `style.css` 
Backend: Flask app (`app.py`) with routes for CRUD + like, JSON file I/O 
Data: `blog_posts.json` in `/static/` (id, author, title, content, likes) 
Deployment: Ready for Render/Heroku/PythonAnywhere (stateless JSON).

## 🚀 Quick Start

```bash
# Clone & install
git clone https://github.com/seb0305/Flask-Blog-App.git
cd Flask-Blog-App
pip install flask

# Run server
python app.py
# Visit http://localhost:5000
```

## 🎮 How to Use
1. View Posts

    Open homepage → See list: "First Post" by John Doe (1 like) → Like/Update/Delete links.

2. Add Post

    Click "Add a New Blog Post" → Fill form (author/title/content) → Submit → Redirects to updated list.

3. Update Post

    Click "Update" on any post → Pre-filled form → Edit → Submit → Back to homepage with changes.

4. Delete Post

    Click "Delete" → Confirms removal → Page refreshes without the post.

5. Like Post

    Click "Like" → Counter increments (e.g. 1 → 2) → Page refreshes.

Sample Data (from blog_posts.json):

- "Fun fact" by Sebastian: "Babies have more bones than adults." (3 likes) 

## 🧠 Core Algorithm
- Data Layer (load_posts/save_posts):

    json.load/dump on static/blog_posts.json – auto ID via max(id)+1. 

- Routes (app.py):

| Route | Method | Action |
|-------|--------|--------|
| `/` | `GET` | List all posts (`render_template('index.html', posts=posts)`) |
| `/add` | `GET/POST` | Show form / Create new post → `redirect(url_for('index'))` |
| `/update/<int:post_id>` | `GET/POST` | Edit form / Update post data |
| `/delete/<int:post_id>` | `GET` | Remove by ID → redirect |
| `/like/<int:post_id>` | `GET` | `post['likes'] += 1` → redirect |

## 📊 Data Schema
```text
erDiagram
    BlogPost {
        int id PK
        string author
        string title
        string content
        int likes
    }
```
Posts stored as JSON array in /static/blog_posts.json. 


## 📝 Development
```bash
# Debug mode
python app.py  # Already debug=True

# Add sample posts manually
# Edit static/blog_posts.json → Restart

# Test routes
curl http://localhost:5000/add
curl -X POST http://localhost:5000/add -d "author=Test&title=Hi&content=Hello"
```
File Structure:

```text
.
├── app.py              # Flask routes + JSON CRUD
├── static/
│   ├── blog_posts.json # Data storage
│   └── style.css       # App styling
├── templates/          # (auto-mounted)
│   ├── index.html
│   ├── add.html
│   └── update.html
└── README.md
```
## 🙌 Contributing
- Fork & clone

- Add new features (comments, auth).

- Improve CSS responsiveness.

- Add form validation (WTForms).

- Write tests (pytest). → Submit PR


## 📄 License
MIT - Free for educational use!