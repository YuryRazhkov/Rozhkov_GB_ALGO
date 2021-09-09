import os

def starter(*args):
    dz_name = f'Rozhkov_Yury_dz_{str(args[0])}'
    task_name = f'task_{str(args[0])}_{str(args[1])}.py'
    if not os.path.exists(dz_name):
        os.makedirs(dz_name)
    task_dz = os.path.join(dz_name, task_name)
    if not os.path.exists(task_dz):
        f = open(task_dz, 'w')
        f.close()


starter(3, 1)
