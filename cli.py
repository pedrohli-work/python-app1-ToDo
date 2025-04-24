"""
Todo List Application

This script allows the user to manage a 
simple to-do list with the following actions:

- Add tasks
- Show tasks
- Edit tasks
- Complete tasks
- Exit the program
"""

# Used to fetch the current time.
import time
# Custom module with helper functions to read/write todos.
import functions

# Gets the current date and time, formats it as a readable string.
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

# Starts an infinite loop to keep the app running until the user chooses to exit.
while True:
    # Prompts the user for input.
    user_action = input("Type add, show, edit, complete or exit:")
    # Removes any leading/trailing whitespace.
    user_action = user_action.strip()

    # Compare and execute the user_action input option
    if user_action.startswith('add'):

        # List slicing the text after the word “add”.
        todo = user_action[4:]

        # Calls a function to read the current list of todos from the file.
        todos = functions.get_todos()

        # Adds the new todo to the list, including a newline character.
        todos.append(todo + '\n')

        # Write and Saves the updated todo list back to the file.
        functions.write_todos(todos)

    # Checks if the user wants to display all todos.
    elif user_action.startswith('show'):
        # Retrieves the current list of todos.
        todos = functions.get_todos()

        # Loops over each todo item with its index.
        for index, item in enumerate(todos):
            # Removes the newline character from each item.
            item = item.strip('\n')
            #Formats and prints each todo.
            row = f"{index + 1}-{item}"
            print(row)

    # Checks if the user wants to edit a todo.
    elif user_action.startswith('edit'):
        # Tries to convert the number from the input to an integer.
        try:
            number = int(user_action[5:])
            print(number)
            # Adjusts the index since list indices start from 0.
            number = number - 1

            # Loads the current todos.
            todos = functions.get_todos()

            # Prompts the user for the new todo content.
            new_todo = input("Enter new todo: ")
            # Updates the selected todo item.
            todos[number] = new_todo + '\n'

            # Saves the updated list.
            functions.write_todos(todos)
        # If the number couldn't be parsed, show error and continue.
        except ValueError:
            print("Your command is not valid")
            continue
    # Checks if the user wants to mark a task as completed.
    elif user_action.startswith('complete'):
        try:
            # Parses the task number to complete.
            number = int(user_action[9:])

            # Loads the current todos.
            todos = functions.get_todos()

            # Adjusts for 0-based indexing.
            index = number -1
            # Gets the todo content to display in a message later.
            todo_to_remove = todos[index].strip('\n')

            # Removes the selected todo from the list.
            todos.pop(index)

            # Saves the updated list.
            functions.write_todos(todos)

            # Prints a confirmation message.
            MESSAGE = f"Todo {todo_to_remove} was removed from the list."
            print(MESSAGE)
        # Catches errors if the given number is out of range.
        except IndexError:
            print("There is no item with that number.")
            continue
    # If the user types "exit", the loop is broken and the program ends.
    elif user_action.startswith('exit'):
        break
    # If the input doesn't match any known command, show error message.
    else:
        print("Command is not valid")

print("Bye!")