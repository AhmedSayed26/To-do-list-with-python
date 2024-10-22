# This repo created by Ahme Sayed
# Task Management System
This is a Python-based Task Management System that allows users to manage personal and work-related tasks. The system provides features like adding tasks, deleting tasks, updating due dates, marking tasks as complete, and saving/loading tasks in JSON format.

# Features
Add Tasks: Supports both personal and work tasks. You can specify task details like title, description, due date, and for personal tasks, category, and for work tasks, priority.
Delete Tasks: Remove tasks by their title.
Show Tasks: View all tasks, including their title, description, due date, status, and specific attributes like category or priority.
Update Due Date: Update the due date of any existing task.
Mark Task as Completed: Mark any task as "complete."
Save and Load: All tasks are saved in a JSON file (data.json) and can be reloaded the next time the program is used.
# How It Works
# 1. Task Types
Personal Task: Includes title, description, due date, and category.
Work Task: Includes title, description, due date, and priority.
General Task: Only includes title, description, and due date.
# 2. Task Manager Operations
The TaskManager class handles all operations for managing tasks:

add_task: Adds a task to the list.
delete_task: Removes a task by its title.
show_tasks: Displays all tasks.
update_due_date: Updates the due date of a task.
mark_task_completed: Marks a task as completed.
save_to_json: Saves the current tasks to a JSON file.
load_from_json: Loads tasks from a JSON file on startup.
# 3. Task Creation
For creating a task, you can specify:

Title
Description
Due Date (with date and time validation)
Category (for personal tasks) or Priority (for work tasks)
# 4. Error Handling
The system provides error handling for:

Invalid date/time formats
Task not found (during deletion or updates)
Invalid input types (during task creation or updates)
# JSON Storage
The tasks are stored in a file called data.json in the following structure:

json
Copy code
[
    {
        "title": "Task Title",
        "description": "Task Description",
        "due_date": "YYYY-MM-DD HH:MM:SS AM/PM",
        "status": "incomplete",
        "category": "Personal/Work (if applicable)",
        "priority": "High/Low (if applicable)"
    }
]
# How to Run the Project
 Install Python: Make sure you have Python installed (Python 3.x recommended).
 Clone the Repository:
 bash
 Copy code
# git clone https://github.com/yourusername/TaskManagementSystem.git
# cd TaskManagementSystem
# Run the Program:
bash
Copy code
python task_manager.py
Follow the Menu: The program will guide you through the menu options like adding tasks, viewing tasks, and so on.
Future Improvements
Add task categories and priorities as optional filters for task viewing.
Add user authentication for task management.
Implement a GUI version using libraries like Tkinter or PyQt.
