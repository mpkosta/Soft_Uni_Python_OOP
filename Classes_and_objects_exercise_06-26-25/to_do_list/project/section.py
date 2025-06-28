from project.task import Task



class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []


    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {Task.details(new_task)} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        task = next((task for task in self.tasks if task.name == task_name), None) #go through and find either what I need or return None
        if task: #if task is not None
            task.completed = True
            return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):

        removed_tasks = 0
        for task in self.tasks:
            if task.completed:
                removed_tasks += 1
                self.tasks.remove(task)
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        result = f"Section {self.name}:"
        for task in self.tasks:
            result += f"\n{Task.details(task)}"
        return result