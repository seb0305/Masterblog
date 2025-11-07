Flask Blog App
This is a simple blog application built with Flask. It allows users to create, view, update, delete, and like blog posts stored in a JSON file.

Features
View all blog posts on the homepage.

Add new blog posts via a form.

Update existing blog posts.

Delete blog posts.

Like blog posts to increment their like count.

Project Structure
app.py: The main Flask application with routes for CRUD operations.

blog_posts.json: JSON file storing blog posts.

Templates:

index.html: Displays all blog posts.

add.html: Form for adding a new post.

update.html: Form for updating a post.

style.css: CSS styles for the application.

Installation
Clone the repository.

Create a virtual environment and activate it.

Install Flask:

text
pip install Flask
Run the app:

text
python app.py
Open your browser and go to http://127.0.0.1:5000/.

Usage
The homepage lists all blog posts with options to like, update, or delete each post.

Use the "Add Post" link to create a new blog post.

Updates and deletions refresh the list automatically.

Notes
All data is stored in blog_posts.json inside the static folder.

Ensure the JSON file has proper read/write permissions.