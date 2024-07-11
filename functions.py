FILEPATH = "todos.txt"

def get_todos(filepath: str = FILEPATH) -> list:
    """
    Get all todos from given filepath

    Args:
        filepath (str, optional): File for TODOs. Defaults to "app1/todos.txt".

    Returns:
        List of todo items.
    """
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos

def write_todos(todos: list, filepath: str = FILEPATH) -> None:
    """
    Write the todo items to given filepath.

    Args:
        todos (list): List of todo items to write
        filepath (str, optional): Path to todos file. Defaults to "app1/todos.txt".
    """
    with open(filepath, "w") as file:
        file.writelines(todos)