#!/usr/bin/env python
# coding: utf-8

# In[ ]:


tasks = []

def add_task(task):
    """
    Add a new task to the to-do
    list
    """
    tasks.append(task)
    print(f"Added task: {task}")

def remove_task(task):
    """
    Remove a task from To-do list
    """
    if task in tasks:
        tasks.remove(task)
        print(f"Removed task: {task}")
    else:
        print(f"{task} not found")

def view_tasks():
    """
    View all tasks in list
    """
    print("To-do list:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

while True:
    print("\nWhat do you want to do?")
    print("1. ADD a task")
    print("2. Remove a task")
    print("3. View all tasks")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        task = input("Enter a new task: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        print("Exiting")
        break
    else:
        print("Invalid choice!")

