tasks = {}


def get_id(tasks_dict: dict) -> int:
    length_tasks = len(tasks)
    return length_tasks + 1


def add_task(name: str = None):
    id_ = get_id(tasks_dict=tasks)
    tasks[id_] = name

def remove_tasks(id_: int):
    tasks.pop(id_)


def sort_tasks():
    for task in tasks: ...


flag = True

while flag:
    action = input('Введите действие: ')
    if action == 'add':
        name = input('Введите название задача: ')
        add_task(name=tasks_name)
        print(tasks)
    if action == 'remove':
        task_id = int(input('Введите id задачи: '))
        remove_tasks(task_id)
    if action == 'show':
        print(tasks)
    if action == 'exit':
        break

print(tasks)
