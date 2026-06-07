"""
validation.py - Input validation functions for the Task Management System.
"""
from datetime import datetime

def validate_task_title(title):
    """
    Validate the task title.
    Args:
        title (str): The task title to validate.
    Returns:
        tuple: (bool, str) - (is_valid, error_message)
    """
    if not isinstance(title, str):
        return False, "Title must be a string."
    if len(title) == 0:
        return False, "Title cannot be empty."
    if len(title) < 3:
        return False, "Title must be at least 3 characters long."
    if len(title) > 100:
        return False, "Title cannot exceed 100 characters."
    return True, ""

def validate_task_description(description):
    """
    Validate the task description.
    Args:
        description (str): The task description to validate.
    Returns:
        tuple: (bool, str) - (is_valid, error_message)
    """
    if not isinstance(description, str):
        return False, "Description must be a string."
    if len(description) == 0:
        return False, "Description cannot be empty."
    if len(description) < 5:
        return False, "Description must be at least 5 characters long."
    if len(description) > 500:
        return False, "Description cannot exceed 500 characters."
    return True, ""

def validate_due_date(due_date):
    """
    Validate the due date string (expected format: YYYY-MM-DD).
    Args:
        due_date (str): The due date string to validate.
    Returns:
        tuple: (bool, str) - (is_valid, error_message)
    """
    if not isinstance(due_date, str):
        return False, "Due date must be a string."
    if len(due_date) == 0:
        return False, "Due date cannot be empty."
    try:
        parsed_date = datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        return False, "Due date must be in YYYY-MM-DD format (e.g., 2024-06-26)."
    return True, ""
