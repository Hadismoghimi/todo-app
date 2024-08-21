FILEPATH = "todo/todos.txt"
# constants
def get_todos(filename=FILEPATH):
    """""
    get_todos returns a list of all todo items from a file and the file is received from argument
    :param filename:file morde nazar
    :return: list of todo items from
    """
    with open(filename, 'r') as file:
        tdos =file.readlines()
    return tdos


def set_todos(todos, filename=FILEPATH):
    """
    set_todos get new todos list and then save in target file
    :param todos:list of todos
    :param filename:target file to save to write todos list
    :return:
    """
    with open(filename, 'w') as file:
        file.writelines(todos)