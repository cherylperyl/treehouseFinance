# Assume you have a Python project, which source code is under a git repo folder
# “my-python-project”. Write a program/script to produce the following statistics of this folder

# a. How many python files

import os
import sys

def count_py_files_in_repos(dir):

    # check if file is a repo
    if os.path.exists(os.path.join(dir,'.git')):
        count = 0

        # get all the files
        for root, dirs, files in os.walk(dir):
            count += len([f for f in files if f.endswith('.py')])
        print(f'{dir} has {count} Python files')

# b. How many lines of code in total, how many lines of comment line (empty line doesn’t count)

# c. How many functions is defined in total

# d. How many lines of changes from the current version against HEAD~3

# e. Total folder size (in MB) per each of the subfolder (down to 2 level depth)