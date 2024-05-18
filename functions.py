def get_todos(filepath_local='todos.txt'):
    with open(filepath_local, 'r') as file_local:
        todos = file_local.readlines()
        return todos

def write_todos(todos_arg, filepath_org = 'todos.txt'):
    with open(filepath_org, 'w') as file_org:
        file_org.writelines(todos_arg)