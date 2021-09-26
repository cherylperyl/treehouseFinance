# Assume you have a Python project, which source code is under a git repo folder
# “my-python-project”. Write a program/script to produce the following statistics of this folder

import os

# e. Total folder size (in MB) per each of the subfolder (down to 2 level depth)
# repo folder is depth 0 (folder with the .git)

def getFolderSize(dir):
    subfolders = {1:[],2:[]}

    for root, dirs, files in os.walk(dir):
        # count number of '/' in the path excluding the main dir, to determine depth
        depth = root[len(dir):].count(os.path.sep) + 1
        if depth <= 2:
            for dir in dirs:
                size = os.path.getsize(os.path.join(root,dir)) * 0.000001
                subfolders[depth].append(size)

    for key, subfolderList in subfolders.items():
        print(f' -------- Depth {key} --------')
        if len(subfolderList) == 0:
            print('There are no subfolders at this level.')
        else:
            print(f'Total size of subfolders: {sum(subfolderList)}')
        for i in range(len(subfolderList)):
            print(f'Size of subfolder {i+1}: {subfolderList[i]}')