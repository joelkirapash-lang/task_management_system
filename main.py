"""
main.py - Entry point for the Task Management System.

Run this script to interact with the task manager via a menu-based interface.
"""

from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress,
)


def print_menu():
    """Display the main menu options."""
    print("\n" + "=" * 40)
    print("       TASK MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add a new task")
    print("2. Mark a task as complete")
    print("3. View pending tasks")
    print("4. Track progress")
    print("5. View all tasks")
    print("6. Exit")
    print("=" * 40)


def display_task(task, index=None):
    """Pretty-print a single task dictionary."""
    prefix = f"[{index}] " if index is not None else ""
    status = "✔ Completed" if task["completed"] else "✘ Pending"
    print(f"\n  {prefix}Title      : {task['title']}")
    print(f"     Description: {task['description']}")
    print(f"     Due Date   : {task['due_date']}")
    print(f"     Status     : {status}")


def handle_add_task(tasks):
    """Prompt the user for task details and add a task."""
    print("\n--- Add a New Task ---")
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()

    success, message = add_task(tasks, title, description, due_date)
    print(f"\n  {message}")


def handle_mark_complete(tasks):
    """Prompt the user for a task title and mark it as complete."""
    print("\n--- Mark Task as Complete ---")
    if not tasks:
        print("\n  No tasks available.")
        return
    title = input("Enter the title of the task to mark as complete: ").strip()
    success, message = mark_task_as_complete(tasks, title)
    print(f"\n  {message}")


def handle_view_pending(tasks):
    """Display all pending (incomplete) tasks."""
    print("\n--- Pending Tasks ---")
    pending = view_pending_tasks(tasks)
    if not pending:
        print("\n  No pending tasks. Great job!")
    else:
        for i, task in enumerate(pending, start=1):
            display_task(task, index=i)


def handle_track_progress(tasks):
    """Display overall task completion progress."""
    print("\n--- Task Progress ---")
    if not tasks:
        print("\n  No tasks recorded yet.")
        return
    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    progress = calculate_progress(tasks)
    print(f"\n  Total tasks    : {total}")
    print(f"  Completed      : {completed}")
    print(f"  Pending        : {total - completed}")
    print(f"  Progress       : {progress:.1f}%")


def handle_view_all(tasks):
    """Display every task regardless of status."""
    print("\n--- All Tasks ---")
    if not tasks:
        print("\n  No tasks recorded yet.")
        return
    for i, task in enumerate(tasks, start=1):
        display_task(task, index=i)


def main():
    """Main loop for the task management system."""
    tasks = []
    print("\nWelcome to the Task Management System!")

    while True:
        print_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            handle_add_task(tasks)
        elif choice == "2":
            handle_mark_complete(tasks)
        elif choice == "3":
            handle_view_pending(tasks)
        elif choice == "4":
            handle_track_progress(tasks)
        elif choice == "5":
            handle_view_all(tasks)
        elif choice == "6":
            print("\nGoodbye! Stay productive!\n")
            break
        else:
            print("\n  Invalid option. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
