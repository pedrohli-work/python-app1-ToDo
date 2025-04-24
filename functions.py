# A constant that stores the path to the file 
# where todos will be read from and written to.
FILEPATH = "todos.txt"


# Defines a function named get_todos that takes an optional parameter filepath. 
# If not provided, it uses the default "todos.txt".
def get_todos(filepath=FILEPATH):
    """Read the list of todos from the 'todos.txt' file 
    and return them as a list of strings.
    """
    # Opens the file in read mode
    with open(filepath, 'r',encoding="utf-8") as file_local:
        # Reads all lines from the file into a list called todos_local.
        todos_local = file_local.readlines()
    # Returns the list of todos
    return todos_local

# Defines a function named write_todos that takes a list of 
# todos and an optional file path.
def write_todos(todos_arg, filepath=FILEPATH):
    """Read the list of todos from the 'todos.txt' file 
    and write them as a list of strings.
    """
    # Opens the file in write mode
    with open(filepath, 'w', encoding="utf-8") as file:
        # Writes the list of todos (todos_arg) to the file.
        file.writelines(todos_arg)


# This code runs only if the file is executed directly (not imported as a module).
if __name__ == "__main__":
    print("Hello")