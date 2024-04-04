class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def complete_task(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1] += " (Completed)"
            print("Task marked as completed!")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
            print("Task deleted successfully!")
        else:
            print("Invalid task index.")


def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            index = int(input("Enter task index to mark as completed: "))
            todo_list.complete_task(index)
        elif choice == "4":
            index = int(input("Enter task index to delete: "))
            todo_list.delete_task(index)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
