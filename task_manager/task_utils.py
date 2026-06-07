"""
task_utils.py - Core task management functions for the Task Management System.
"""

from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)


def add_task(tasks, title, description, due_date):
    """
    Add a new task to the tasks list after validating all inputs.

    Args:
        tasks (list): The current list of task dictionaries.
        title (str): The title of the new task.
        description (str): The description of the new task.
        due_date (str): The due date of the new task (YYYY-MM-DD).

    Returns:
        tuple: (bool, str) - (success, message)
    """
    is_valid, error = validate_task_title(title)
    if not is_valid:
        return False, f"Invalid title: {error}"

    is_valid, error = validate_task_description(description)
    if not is_valid:
        return False, f"Invalid description: {error}"

    is_valid, error = validate_due_date(due_date)
    if not is_valid:
        return False, f"Invalid due date: {error}"

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False,
    }
    tasks.append(task)
    return True, "Task added successfully!"


def mark_task_as_complete(tasks, title):
    """
    Mark an existing task as complete by its title.

    Args:
        tasks (list): The current list of task dictionaries.
        title (str): The title of the task to mark as complete.

    Returns:
        tuple: (bool, str) - (success, message)
    """
    for task in tasks:
        if task["title"].lower() == title.lower():
            if task["completed"]:
                return False, f"Task '{task['title']}' is already marked as complete!"
            task["completed"] = True
            return True, f"Task '{task['title']}' marked as complete!"
    return False, f"No task found with the title '{title}'."


def view_pending_tasks(tasks):
    """
    Return a list of all tasks that are not yet completed.

    Args:
        tasks (list): The current list of task dictionaries.

    Returns:
        list: A list of pending (incomplete) task dictionaries.
    """
    pending = [task for task in tasks if not task["completed"]]
    return pending


def calculate_progress(tasks):
    """
    Calculate the percentage of tasks that have been completed.

    Args:
        tasks (list): The current list of task dictionaries.

    Returns:
        float: The completion percentage (0.0 to 100.0).
               Returns 0.0 if there are no tasks.
    """
    if len(tasks) == 0:
        return 0.0
    completed_count = sum(1 for task in tasks if task["completed"])
    return (completed_count / len(tasks)) * 100
