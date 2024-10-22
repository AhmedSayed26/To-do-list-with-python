import json
from datetime import datetime
import time

f_delet = 0
f_complete = 0
f_update = 0


def get_date():
    while True:

        date_str = input("Enter the task date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date_str, "%Y-%m-%d")

            return date_str
        except ValueError:
            print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")


def get_time():
    while True:

        time_str = input("Enter the task time (HH:MM AM/PM): ")
        try:
            datetime.strptime(time_str, "%I:%M %p")
            return time_str

        except ValueError:
            print("Invalid time format. Please enter the time in the format HH:MM AM/PM.")


def get_task_date():
    date_str = get_date()
    time_str = get_time()

    while True:
        try:
            due_date_time_str = date_str + " " + time_str
            due_date_time = datetime.strptime(due_date_time_str, "%Y-%m-%d %I:%M %p")
            formatted_due_date = due_date_time.strftime("%Y-%m-%d %I:%M:%S %p")
            return formatted_due_date
        except ValueError:
            print("Invalid date or time. Please try entering the time again.")
            time_str = get_time()


class Task:
    def __init__(self, title, description, due_date, status="incomplete"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_completed(self):
        self.status = "complete"

    def update_due_date(self, new_date):
        self.due_date = new_date

    def view_detail(self):
        return (f"Task title  : {self.title}\n"
                f"Description : {self.description}\n"
                f"Due date    : {self.due_date}\n"
                f"Status      : {self.status}\n")

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }


class PersonalTask(Task):
    def __init__(self, title, description, due_date, category, status="incomplete"):
        super().__init__(title, description, due_date, status)
        self.category = category

    def view_detail(self):
        details = super().view_detail()
        return details + f"Category  : {self.category}\n"

    def to_dict(self):
        data = super().to_dict()
        data["category"] = self.category
        return data


class WorkTask(Task):
    def __init__(self, title, description, due_date, priority, status="incomplete"):
        super().__init__(title, description, due_date, status)
        self.priority = priority

    def view_detail(self):
        details = super().view_detail()
        return details + f"Priority  : {self.priority}\n"

    def to_dict(self):
        data = super().to_dict()
        data["priority"] = self.priority
        return data


class TaskManager:
    def __init__(self):
        self.tasks = []

    def search_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def add_task(self, task):
        self.tasks.append(task)
        print("------------------------------------------------------------>")
        print("Task Add Done.")
        print("------------------------------------------------------------>")
        time.sleep(2)

    def delete_task(self, title):
        global f_delet
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                f_delet = 1
        if f_delet == 1:
            print("------------------------------------------------------------>")
            print("Task Deletion Done.")
            print("------------------------------------------------------------>")
            time.sleep(2)
        elif f_delet == 0:
            print("------------------------------------------------------------>")
            print("Error: Task title not found. Enter correct title.")
            print("------------------------------------------------------------>")
            time.sleep(2)

    def show_tasks(self):
        if len(self.tasks) == 0:
            print("There are no tasks yet.")
            return 0
        print("------------------------------------------------------------>")
        for task in self.tasks:
            print(task.view_detail())
            print("------------------------------------------------------------>")
        time.sleep(3)

    def update_due_date(self, title, new_date):
        global f_update
        task = self.search_task(title)
        if task is None:
            print("------------------------------------------------------------>")
            print("Error: Task title not found. Enter correct title.")
            print("------------------------------------------------------------>")
            time.sleep(2)
        else:
            task.update_due_date(new_date)
            print("------------------------------------------------------------>")
            print("Task Update Due Date Done.")
            print("------------------------------------------------------------>")
            f_update = 1
            time.sleep(2)

    def mark_task_completed(self, title):
        global f_complete
        task = self.search_task(title)
        if task is None:
            print("------------------------------------------------------------>")
            print("Error: Task title not found. Enter correct title.")
            print("------------------------------------------------------------>")
            time.sleep(2)
        else:
            task.mark_completed()
            print("------------------------------------------------------------>")
            print("Task Mark Complete Done.")
            print("------------------------------------------------------------>")
            f_complete = 1
            time.sleep(2)

    def save_to_json(self, filename="data.json"):
        tasks_data = [task.to_dict() for task in self.tasks]
        with open(filename, "w") as file:
            json.dump(tasks_data, file, indent=4)

    def load_from_json(self, filename="data.json"):
        try:
            with open(filename, "r") as file:
                tasks_data = json.load(file)
                for task_data in tasks_data:
                    if "priority" in task_data:
                        task = WorkTask(**task_data)
                    elif "category" in task_data:
                        task = PersonalTask(**task_data)
                    else:
                        task = Task(**task_data)
                    self.tasks.append(task)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Error loading tasks from JSON or file is empty on first use.")
            time.sleep(2)
            print("------------------------------------------------------------>")


def main():
    manager = TaskManager()
    manager.load_from_json()

    global f_delet
    global f_complete
    global f_update

    while True:
        print("1. Add Task\n2. Delete Task\n3. Show Tasks\n4. Update Due Date\n5. Mark Task Completed\n6. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task_type = input("Enter task type (personal/work): ")
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = get_task_date()

            if task_type == "personal":
                category = input("Enter category: ")
                task = PersonalTask(title, description, due_date, category)
            elif task_type == "work":
                priority = input("Enter priority: ")
                task = WorkTask(title, description, due_date, priority)
            else:
                task = Task(title, description, due_date)

            manager.add_task(task)

        elif choice == "2":
            while f_delet == 0:
                title = input("Enter the title of the task to delete: ")
                manager.delete_task(title)
            f_delet = 0

        elif choice == "3":
            manager.show_tasks()

        elif choice == "4":
            while f_update == 0:
                title = input("Enter the title of the task to update: ")
                new_date = get_task_date()
                manager.update_due_date(title, new_date)
            f_update = 0

        elif choice == "5":
            while f_complete == 0:
                title = input("Enter the title of the task to mark as completed: ")
                manager.mark_task_completed(title)
            f_complete = 0

        elif choice == "6":
            manager.save_to_json()
            break

        else:
            print("Invalid choice. Please try again.")


main()
