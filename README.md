# Flask To-Do List Application

A simple to-do list application built using Flask and SQLite, allowing users to add, update, and delete tasks. This project demonstrates the basics of using Flask with SQLAlchemy for database management, templating with Jinja2, and basic styling with HTML and CSS.

## Features

- **Add tasks**: Enter a task and click "Add Task" to save it to the database.
- **View tasks**: See all tasks displayed in a table format with timestamps.
- **Update tasks**: Click "Update" to edit an existing task.
- **Delete tasks**: Click "Delete" to remove a task from the database.

## Project Structure

```sh
.
├── app.py
├── README.md
├── requirements.py
├── requirements.txt
├── static
│   └── css
│       └── main.css
├── templates
│   ├── base.html
│   ├── index.html
│   └── update.html
└── test.db
```

## Prerequisites

- **Python 3.x**
- **Flask**: Install with `pip install Flask`
- **Flask-SQLAlchemy**: Install with `pip install Flask-SQLAlchemy`

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/flask-todo-app.git
   cd flask-todo-app
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Initialize the database by running ```requirements.py```:

   ```bash
   python3 requirements.py
   ```

4. Start the Flask application:

   ```bash
   python3 app.py
   ```

5. Open your web browser and go to ```<http://127.0.0.1:5000>```.

## Project Files

- ```app.py```: The main Flask application, defining routes, the database model, and app configuration.
- ```requirements.py```: A helper script to initialize the database and create necessary tables.
- ```static/css/main.css```: Contains the CSS styling for the application.
- ```templates/```: Directory containing HTML templates (base.html, index.html, update.html) for rendering the UI.

## References

This project was inspired by the tutorial on freeCodeCamp.org:

- [Build a To-Do List App with Flask and Python](https://www.youtube.com/watch?v=Z1RJmh_OqeA&list=WL&index=5&ab_channel=freeCodeCamp.org)
