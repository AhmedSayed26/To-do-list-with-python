# This repo created by Ahme Sayed
# To-Do-List with Python
This is a Python-based To-Do List Application designed to help users manage personal and work-related tasks efficiently. It provides features like adding tasks, deleting tasks, updating due dates, marking tasks as complete, and saving/loading tasks from a JSON file.

# Features
Add Tasks: Create both personal and work tasks with attributes such as title, description, due date, and additional attributes like category (for personal tasks) or priority (for work tasks).
Delete Tasks: Remove tasks based on their title.
Show Tasks: View details of all tasks including their title, description, due date, status, and other relevant information.
Update Due Date: Modify the due date of any task.
Mark Task as Completed: Change the status of tasks to "complete."
Save and Load: Tasks are stored in data.json and can be loaded when the program restarts.
How It Works
# 1. Task Types
Personal Task: Includes task title, description, due date, and category.
Work Task: Includes task title, description, due date, and priority.
General Task: Includes only title, description, and due date.
# 2. Task Manager Operations
The TaskManager class is responsible for managing the following operations:

add_task: Add new tasks to the list.
delete_task: Remove a task by its title.
show_tasks: Display all tasks in a structured format.
update_due_date: Update the due date of a specific task.
mark_task_completed: Mark a task as "completed."
save_to_json: Save all tasks to a JSON file.
load_from_json: Load tasks from the JSON file at startup.
# 3. Task Creation
To create a task, the user provides:

Title
Description
Due Date (validated input)
Category (for personal tasks) or Priority (for work tasks)
# 4. Error Handling
The application provides error handling for:

Invalid date and time formats.
Non-existent tasks (when attempting to delete or update).
Invalid inputs during task creation or updating.
# JSON Storage
Tasks are stored in a data.json file with the following structure:

json
Copy code
[
    {
        "title": "Sample Task",
        "description": "This is a task description",
        "due_date": "YYYY-MM-DD HH:MM AM/PM",
        "status": "incomplete",
        "category": "Personal (if applicable)",
        "priority": "High (if applicable)"
    }
]
# How to Run the Project
Install Python: Ensure Python (3.x recommended) is installed.
Clone the Repository:
bash
Copy code
# git clone https://github.com/AhmedSayed26/to-do-list-with-python.git
cd to-do-list
Run the Program:
bash
Copy code
python task_manager.py
Menu Options: The program provides an interactive menu for adding, deleting, updating, and viewing tasks.
Future Improvements
Add filtering options to view tasks based on categories or priorities.
Implement a user authentication system to manage tasks for multiple users.
Develop a graphical user interface (GUI) using Tkinter or PyQt.
