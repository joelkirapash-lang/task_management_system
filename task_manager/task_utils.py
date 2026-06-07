"""
task_utils.py - Core task management functions for the Task Management System.
"""

from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)


def add_task(tasks, title, description, due_date):
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


def mark_task_as_complete(tasks, identifier):
    if len(tasks) == 0:
        return False, "No tasks available."
    try:
        index = int(identifier) - 1
        if 0 <= index < len(tasks):
            task = tasks[index]
            if task["completed"]:
                return False, f"Task already complete!"
            task["completed"] = True
            return True, f"Task marked as complete!"
    except ValueError:
        pass
    for task in tasks:
        if task["title"].lower() == identifier.lower():
            if task["completed"]:
                return False, f"Task already complete!"
            task["completed"] = True
            return True, f"Task marked as complete!"
    return False, f"No task found with the title or number: {identifier}."


def view_pending_tasks(tasks):
    if len(tasks) == 0:
        return []
    pending = [task for task in tasks if not task["completed"]]
    return pending


def calculate_progress(tasks):
    if len(tasks) == 0:
        return 0.0
    completed_count = sum(1 for task in tasks if task["completed"])
    return (completed_count / len(tasks)) * 100
