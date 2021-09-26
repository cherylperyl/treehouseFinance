# Assume you have a Python project, which source code is under a git repo folder
# “my-python-project”. Write a program/script to produce the following statistics of this folder

import os

# b. How many lines of code in total, how many lines of comment line (empty line doesn’t count)
# assumption: only count code and comment lines in .py files
# assumption: if a line only contains '#', it is also counted as a comment line
# assumption: if a line only contains "'''", it is also counted as a comment line
# assumption: all python files can run without any syntax error (eg. no missing ending "'''" for code blocks)

def countLines(dir):

    codeLines = 0
    commentLines = 0
    blockCode = False

    for root, dirs, files in os.walk(dir):
        files = [f for f in files if (f.endswith('.py') and f != 'tempCodeRunnerFile.py')]

        # if files list is empty, means that current root has no .py files with code
        if files != []:
            for file in files:

                # specify file directory by joining root to file name
                fileDir = os.path.join(root,file)
                with open (fileDir, 'r') as f:
                    for line in f:

                        # remove lines with spaces and lines with '\n' (exists when <enter> is pressed)
                        line = line.strip().strip('\n')

                        # catch comment lines that starts with '#'
                        # and comment lines that trails after code
                        if line.startswith('#') or (('#' in line) and ("'#'" not in line) and ('"#"' not in line)):
                            commentLines += 1
                        
                        # catch a block of comment that starts with "'''"
                        if line.startswith("'''"):
                            blockCode = True
                        if line.endswith("'''") and blockCode:
                            commentLines += 1
                            blockCode = False
                        if blockCode:
                            commentLines += 1

                        # the rest would be code lines
                        elif line != '' and not line.startswith("'''") and not line.startswith('#'):
                            codeLines += 1

    print(f'This git repo contains {codeLines} lines of code and {commentLines} lines of comments.')

