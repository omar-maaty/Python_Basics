import os

def add_task(task):
    with open('tasks.txt','a') as f :
        f.write(f'{task}\n')
        print('tha task added successfully\n')

def view_task():
    print('\n----Your Tasks----')
    with open('tasks.txt','r') as f:
        lines=f.readlines()
        if not lines:
            print('No Task Added')
        else:
            for i, line in enumerate(lines,1):
                print(f'{i}- {line.strip()}')
        print('-------------------')


def delete_task(indx):
    if not os.path.exists('tasks.txt'):
        print('No Tasks to delete')
        return
    with open('tasks.txt','r') as f:
        tasks=[line.strip() for line in f.readlines()]
    if indx<=len(tasks):
        tasks.pop(indx-1)
        print('The task deleted successfully\n')
        with open('tasks.txt','w') as f:
            for tsk in tasks:
                f.write(tsk+'\n')
    else:
        print('enter a valid index')


if not os.path.exists('tasks.txt'):
    os.system('touch tasks.txt')

try:
    while True:
        op=int(input('choose operation from: \n'
                     '1- Add a Task\n'
                     '2- View All Tasks\n'
                     '3- Marks As Done\n'
                     'choose: '))
        if op==1:
            t=input('Add new task: ')
            t.strip()
            add_task(t)

        elif op==2:
            view_task()

        elif op==3:
            del_task=int(input('Write the number of task what you finished it:'))
            delete_task(del_task)
        else:
            print('enter a valid number(operation[1 , 2 or 3])')
except ValueError:
    print('Enter valid number')
