"""
GUI version of the To-Do application using PySimpleGUI.

This script provides a graphical interface for managing a to-do list,
including adding, editing, and completing tasks. Tasks are saved to a
local file called 'todos.txt'.
"""

import time
import os
import FreeSimpleGUI as sg
import functions

# Checks if the todos.txt file exists.
# If not, creates an empty file to avoid errors later.
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w", encoding="utf-8") as file:
        pass

# Sets the visual theme of the GUI to “DarkBlack”.
sg.theme("DarkBlack")

# Creates a text element for showing the current time.
clock = sg.Text('', key='clock')
# Label prompting the user to enter a task.
label = sg.Text("Type in a To-Do")
# Input field where the user can type a new todo.
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
# Button labeled “Add” to add a new todo.
add_button = sg.Button("Add")
# Listbox showing the current todos.
list_box = sg.Listbox(values=functions.get_todos(), key='todos', 
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# Constructs the GUI window with the title “My To-Do App”.
# Lays out the elements in rows.
window = sg.Window('My To-Do App', 
                   layout=[[clock], 
                           [label], 
                           [input_box, add_button], 
                           [list_box, edit_button, complete_button], 
                           [exit_button]],
                   font=('Helvetica', 20))

# Starts the event loop. 
# It reads user actions and the state of all inputs every 200 milliseconds.
while True:
    event, values = window.read(timeout=200)
    if event == sg.WIN_CLOSED:
        break
    # Updates the clock element with the current time on each loop.
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
     
    match event:
        case "Add":
            # Calls the get_todos() function to 
            # load the current list of todos from the file (todos.txt).
            todos = functions.get_todos()
            # Retrieves the text entered in the input box 
            # (whose key is "todo") from the values dictionary.
            new_todo = values['todo'] + "\n"
            # Adds the new todo to the list of todos in memory.
            todos.append(new_todo)
            # Calls the write_todos() function to save the updated list 
            # (including the new item) back to todos.txt.
            functions.write_todos(todos)
            # Refreshes the listbox in the GUI so it shows the updated list of todos, 
            # including the one that was just added.
            window['todos'].update(values=todos)
            #Update the input text
            window['todo'].update(value='')
        case "Edit":
            try:
                # Retrieves the currently selected todo from the listbox.
                todo_to_edit = values['todos'][0]
                # Gets the new text the user entered in the input box
                new_todo = values['todo'] + "\n"
                # Loads the current list of todos from the file.
                todos = functions.get_todos()
                # Finds the position/index of the selected todo in the list.
                index = todos.index(todo_to_edit)
                # Replaces the selected todo in the list with the new version.
                todos[index] = new_todo
                # Saves the updated list of todos back to the file.
                functions.write_todos(todos)
                # Updates the listbox in the GUI to reflect the changes.
                window['todos'].update(values=todos)
                #Update the input text
                window['todo'].update(value='')
            # If no item is selected, shows a popup warning.
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))       
        case "Complete":
            try:
                #Getting the todo to be completed extracting the value from dictionary Values.
                todo_to_complete = values['todos'][0]
                #Get the todos from the todos.txt using functions
                todos = functions.get_todos()
                #Remove the todo from the list
                todos.remove(todo_to_complete)
                #Write the new list of todos in todos.txt
                functions.write_todos(todos)
                #Update the todos list box with the current value.
                window['todos'].update(values=todos)
                #Update the input text
                window['todo'].update(value='')
            # Handles the case when no item is selected.
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))

        # Closes the app if user clicks "Exit".
        case 'Exit':
            break
        
        # Updates the input box with the selected todo for easy editing.
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        # Handles the user clicking the window close (X) button.    
        case sg.WIN_CLOSED:
            break

# Closes the GUI window after the loop ends.
window.close()
