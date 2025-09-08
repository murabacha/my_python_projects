from rich.console import Console
from rich.table import Table

console = Console()

def view_tasks(tasks):
    table = Table(title="To-Do List")
    table.add_column("No.", style="cyan", justify="right")
    table.add_column("Task", style="magenta")
    table.add_column("Deadline", style="green")

    for i, task in enumerate(tasks, start=1):
        name, deadline = task.strip().split(" - ")
        table.add_row(str(i), name, deadline)

    console.print(table)

tasks = [
    "task name {Buy milk} - completion time {Monday at 14:00 hours}",
    "task name {Study regex} - completion time {Tuesday at 09:00 hours}"
]

view_tasks(tasks)
