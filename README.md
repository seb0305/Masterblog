# Flask Blog App
## About
This project is a simple blog application built using the Flask web framework. It allows users to view, add, update, delete, and like blog posts stored in a JSON file.

## Features
- Display all blog posts on the homepage.

- Add new posts through a dedicated form.

- Update existing posts.

- Delete posts.

- Like posts to increment their like count.

## Project Structure
app.py - The main Flask application, handling routes and post data management.

blog_posts.json - JSON storage file holding the blog posts data.

### HTML Templates:

index.html - Displays the list of all posts.

add.html - Form to add a new blog post.

update.html - Form to edit an existing blog post.

style.css - Styling for the app's web pages.

## Installation
### Prerequisites
Python 3.7+

Flask

### Setup Instructions
1. Clone the repository:
git clone https://github.com/seb0305/Masterblog.git
cd Masterblog
2. (Optional) Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3. Install dependencies:
pip install Flask
4. Run the app:
python app.py
5. Open your browser and visit http://127.0.0.1:5000/ to access the blog.

## Usage 
- The homepage lists all blog posts with options to like, update, or delete each.

- Use the "Add Post" link to create new posts.

- Updates and deletions refresh immediately on the homepage.

## Notes
All posts are stored in blog_posts.json in the static folder.

Make sure the JSON file has proper read/write permissions.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.