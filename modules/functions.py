FILE_PATH = "files/todos.txt"


def get_todos(filepath=FILE_PATH):
    """
    function reads the given or default file and return todos from the file

    returns a list
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


# print(help(get_todos))

def save_todos(todos_to_save, filepath=FILE_PATH):
    with open(filepath, "w") as file_to_save:
        file_to_save.writelines(todos_to_save)


if __name__ == "__main__":
    print(get_todos())
