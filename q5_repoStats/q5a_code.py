# Assume you have a Python project, which source code is under a git repo folder
# “my-python-project”. Write a program/script to produce the following statistics of this folder

# a. How many python files
# assumption: python files do not include '.ipynb'

import os

def countPyFiles(dir):
    count = 0

    # get all the files located in the input directory
    '''
    root - directories only from what you specified
    dirs - sub-directories from root
    files - all files from root and dirs
    '''
    for root, dirs, files in os.walk(dir):
        for f in files:
            if f.endswith('.py') and f != 'tempCodeRunnerFile.py':
                count += 1

    print(f'This git repo directory has {count} Python files.')