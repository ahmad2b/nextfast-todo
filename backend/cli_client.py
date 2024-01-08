import requests
import json

API_URL = "http://localhost:8000"  # replace with your API URL


def get_todos():
    response = requests.get(f"{API_URL}/todos")
    todos = response.json()
    for todo in todos:
        print(
            f"ID: {todo['id']}, Title: {todo['title']}, Completed: {todo['completed']}"
        )


def get_todo(todo_id):
    response = requests.get(f"{API_URL}/todos/{todo_id}")
    todo = response.json()
    print(f"ID: {todo['id']}, Title: {todo['title']}, Completed: {todo['completed']}")


def create_todo(title, description, completed):
    todo = {"title": title, "description": description, "completed": completed}
    response = requests.post(f"{API_URL}/todos", json=todo)
    if response.status_code == 201:
        print("Todo created successfully")
    else:
        print("Error: Could not create todo")


def update_todo(todo_id, title, description, completed):
    todo = {"title": title, "description": description, "completed": completed}
    response = requests.put(f"{API_URL}/todos/{todo_id}", json=todo)
    if response.status_code == 200:
        print("Todo updated successfully")
    else:
        print("Error: Could not update todo")


def delete_todo(todo_id):
    response = requests.delete(f"{API_URL}/todos/{todo_id}")
    if response.status_code == 204:
        print("Todo deleted successfully")
    else:
        print("Error: Could not delete todo")


# Test the functions
print("Get all todos")
get_todos()

print("\nGet a todo")
get_todo(25)

print("\nCreate a todo")
create_todo("Test Todo", "This is a test todo", False)

print("\nGet all todos after creation")
get_todos()

print("\nUpdate a todo")
update_todo(25, "Updated Test Todo", "This is an updated test todo", True)

print("\n Delete a todo")
delete_todo(25)
