"""
Web version of the To-Do application using Streamlit.

Allows users to view, add, and complete to-dos via a browser interface.
"""

import streamlit as st
import functions

# Loads the current list of todos from the file.
todos = functions.get_todos()

def add_todo():
    """Add a new todo from the input field to the list and save it."""
    # Retrieves the text from the input field (stored in session_state).
    new_todo = st.session_state["new_todo"] + "\n"
    # Appends the new todo to the list.
    todos.append(new_todo)
    # Saves the updated list back to the file.
    functions.write_todos(todos)

# Sets the main title of the web app.
st.title("My Todo App")
# Sets a subtitle.
st.subheader("This is my todo app.")
# Adds a short description text.
st.write("This app is to increase your productivity.")

# Loops over the todos with their index.
for index, todo in enumerate(todos):
    # Creates a checkbox for each todo item
    checkbox = st.checkbox(todo, key=todo)
    # Checks if the user marked the checkbox.
    if checkbox:
        # Removes the checked todo from the list.
        todos.pop(index)
        # Saves the updated list after removing the item.
        functions.write_todos(todos)
        # Removes the checkbox’s state from session_state to avoid glitches on rerun.
        del st.session_state[todo]
        # Refreshes the page to immediately reflect the changes
        st.rerun()

# A text input where the user can type a new todo.
# When the input changes (i.e., user presses Enter), it calls the add_todo() function.
# The input is stored in session_state['new_todo'].
st.text_input(label="Add new To Do", placeholder="Press enter to add it.", 
              on_change=add_todo, key='new_todo')
