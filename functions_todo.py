FILEPATH = "todos.txt"
# it's in uppercase to show that this is a constant used in this function
# usually these are defined at the top of the program


def get_todos(filepath=FILEPATH):
    # here todos.txt is default parameter
    # by not defining the filepath hard-coded, we can make this custom function more dynamic
    # here filepath is a parameter
    """ Read a text file and return the list of
    to-do items."""
    # called doc string
    # It's recommended to use doc string in the function
    # - helpful to create help file to read later on.
    # It is useful where multiple programs run together
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
# print(help(get_todos))


def write_todos(todos_arg, filepath=FILEPATH):
    # when we are defining default parameter, the undefined argument should be in the first
    # - order of these arguments are important - not only here, while calling the function also
    # here todos_arg is the content needs to be written in the filepath
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
    return None
    # because role of this function is to behave as a procedure

