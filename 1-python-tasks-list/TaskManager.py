import os
import json
import uuid
from datetime import datetime

# -------------------------
# Excepciones personalizadas
# -------------------------
class TaskNotFoundError(Exception):
    def __init__(self, task_id):
        super().__init__(f"Task with ID {task_id} not found.")

class InvalidTaskIdError(Exception):
    def __init__(self):
        super().__init__("Invalid task ID provided.")

# -------------------------
# Gestor de Tareas
# -------------------------
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.file_name = "tasks.json"
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, "r") as file:
                    self.tasks = json.load(file)
            except:
                print("Error loading task data. Starting with empty task list.")
                self.tasks = []

    def save_tasks(self):
        with open(self.file_name, "w") as file:
            json.dump(self.tasks, file, indent=2)

    def add_task(self, title, description):
        task = {
            "id": str(uuid.uuid4()),
            "title": title,
            "description": description,
            "status": "Pending",
            "created_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully!")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        self.display_tasks(self.tasks)

    def filter_by_status(self, status):
        filtered = [t for t in self.tasks if t["status"].lower() == status.lower()]
        if not filtered:
            print(f"No tasks found with status '{status}'.")
        else:
            self.display_tasks(filtered)

    def filter_by_keyword(self, keyword):
        keyword = keyword.lower()
        filtered = [
            t for t in self.tasks
            if keyword in t["title"].lower() or keyword in t["description"].lower()
        ]
        if not filtered:
            print(f"No tasks found with keyword '{keyword}'.")
        else:
            self.display_tasks(filtered)

    def edit_task(self, task_id, new_title=None, new_description=None):
        task = next((t for t in self.tasks if t["id"] == task_id), None)
        if not task:
            raise TaskNotFoundError(task_id)

        if new_title:
            task["title"] = new_title
        if new_description:
            task["description"] = new_description

        self.save_tasks()
        print(f"Task '{task['id']}' updated successfully!")

    def mark_complete(self, task_id):
        task = next((t for t in self.tasks if t["id"] == task_id), None)
        if not task:
            raise TaskNotFoundError(task_id)
        task["status"] = "Completed"
        self.save_tasks()
        print(f"Task '{task['title']}' marked as completed!")

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                removed = self.tasks.pop(i)
                self.save_tasks()
                print(f"Task '{removed['title']}' deleted successfully!")
                return
        raise TaskNotFoundError(task_id)

    def display_tasks(self, task_list):
        print("\n" + "=" * 120)
        print(f"{'ID':<38} {'TITLE':<20} {'STATUS':<10} {'CREATED DATE':<20} {'DESCRIPTION':<30}")
        print("-" * 120)
        for task in task_list:
            print(f"{task['id']:<38} {task['title'][:18]:<20} {task['status']:<10} {task['created_date']:<20} {task['description'][:28]:<30}")
        print("=" * 120 + "\n")

# -------------------------
# Interfaz CLI
# -------------------------
def main():
    task_manager = TaskManager()

    while True:
        print("\nTASK MANAGER")
        print("1. Add Task")
        print("2. List All Tasks")
        print("3. Filter Tasks")
        print("4. Edit Task")
        print("5. Mark Task as Complete")
        print("6. Delete Task")
        print("7. View DataBase")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        try:
            if choice == "1":
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                task_manager.add_task(title, description)

            elif choice == "2":
                task_manager.list_tasks()

            elif choice == "3":
                print("\nFilter Options:")
                print("1. By Status")
                print("2. By Keyword")
                filter_choice = input("Choose filter type (1-2): ")
                if filter_choice == "1":
                    status = input("Enter status (Pending/Completed): ")
                    task_manager.filter_by_status(status)
                elif filter_choice == "2":
                    keyword = input("Enter keyword to search: ")
                    task_manager.filter_by_keyword(keyword)
                else:
                    print("Invalid filter option.")

            elif choice == "4":
                task_id = input("Enter task ID to edit: ")
                new_title = input("Enter new title (leave blank to keep current): ")
                new_description = input("Enter new description (leave blank to keep current): ")
                task_manager.edit_task(
                    task_id,
                    new_title if new_title.strip() else None,
                    new_description if new_description.strip() else None
                )

            elif choice == "5":
                task_id = input("Enter task ID to mark as complete: ")
                task_manager.mark_complete(task_id)

            elif choice == "6":
                task_id = input("Enter task ID to delete: ")
                task_manager.delete_task(task_id)
                
            elif choice == "7":
                 if os.path.exists(task_manager.file_name):
                    print("\nContent of tasks.json:")
                    with open(task_manager.file_name, "r") as file:
                        data = json.load(file)
                        print(json.dumps(data, indent=2))

            elif choice == "8":
                print("Exiting Task Manager. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
