# Assume you have a Python project, which source code is under a git repo folder
# “my-python-project”. Write a program/script to produce the following statistics of this folder

import os

# c. How many functions is defined in total
# assumption: only count functions in .py files
# assumption: all python files can run without any syntax error (eg. no incorrectly defined functions)

def countFuncs(dir):

    count = 0

    for root, dirs, files in os.walk(dir):
        files = [f for f in files if (f.endswith('.py') and f != 'tempCodeRunnerFile.py')]

        # if files list is empty, means that current root has no .py files with code
        if files != []:
            for file in files:

                # specify file directory by joining root to file name
                fileDir = os.path.join(root,file)
                with open (fileDir, 'r') as f:
                    for line in f:

                        # remove spaces in front of lines
                        # this is to catch functions that are defined in functions (though this is not a recommended practice)
                        line = line.strip()
                        if line.startswith('def'):
                            count += 1

    print(f'This git repo contains {count} defined functions.')