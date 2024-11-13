"""
Flask To-Do Application

This script initializes a Flask application with SQLAlchemy to manage
a simple to-do list, where users can add, update, and delete tasks.
"""

import os
from datetime import datetime, timezone
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure SQLite database URI
# Use three slashes (///) for relative paths and four (////) for absolute paths
db_path = os.path.join(os.path.abspath(os.getcwd()), "test.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)


class Todo(db.Model):
    """
    Todo Model

    Represents a task in the to-do list.
    Attributes:
        id (int): The primary key for the task.
        content (str): The task description, provided by the user.
        completed (int): Indicates if the task is completed (0 by default).
        date_created (datetime): The timestamp when the task was created.
    """

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        """
        String representation of the Todo model.
        This is useful for debugging and logging.

        Returns:
            str: A string indicating the task ID.
        """
        return f"<Task {self.id}>"


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Main route for displaying and adding tasks.

    GET: Fetch and display all tasks in the to-do list.
    POST: Create a new task from form input and add it to the database.

    Returns:
        str: Rendered HTML template for the main page.
    """
    if request.method == "POST":
        # Get the task content from the form input
        task_content = request.form.get("content")

        # Validate that content is not empty
        if not task_content:
            return redirect(url_for("index"))

        # Create a new task and add it to the database
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for("index"))
        except Exception as e:
            print(f"Error adding task: {e}")
            return "There was an issue adding your task."

    # Fetch all tasks for display on the page
    tasks = Todo.query.order_by(Todo.date_created).all()
    return render_template("index.html", tasks=tasks)


@app.route("/delete/<int:task_id>")
def delete(task_id):
    """
    Route for deleting a specific task by its ID.

    Args:
        task_id (int): The ID of the task to delete.

    Returns:
        str: Redirect to the main page after deletion.
    """
    task_to_delete = Todo.query.get_or_404(task_id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect(url_for("index"))
    except Exception as e:
        print(f"Error deleting task {task_id}: {e}")
        return "There was an issue deleting the task."


@app.route("/update/<int:task_id>", methods=["GET", "POST"])
def update(task_id):
    """
    Route for updating a specific task by its ID.

    GET: Display the update form pre-filled with current task details.
    POST: Update the task in the database with the new content.

    Args:
        task_id (int): The ID of the task to update.

    Returns:
        str: Rendered HTML template for the update page.
    """
    task = Todo.query.get_or_404(task_id)

    if request.method == "POST":
        task_content = request.form.get("content")

        # Update the task content if it's not empty
        if task_content:
            task.content = task_content
            try:
                db.session.commit()
                return redirect(url_for("index"))
            except Exception as e:
                print(f"Error updating task {task_id}: {e}")
                return "There was an issue updating the task."
        else:
            print("Update failed: content is empty.")
            return redirect(url_for("update", task_id=task_id))

    return render_template("update.html", task=task)


if __name__ == "__main__":
    # Run the app in debug mode for development purposes
    app.run(debug=True)
