import os
my_directory = {'my_project' : ['settings', 'mainapp', 'adminapp', 'authapp']}
for root, folders in my_directory.items():
    if os.path.exists(root):
        print(root, 'уже есть')
    else:
        for folder in folders:
            cur_dir = os.path.join(root, folder)
            os.makedirs(cur_dir)