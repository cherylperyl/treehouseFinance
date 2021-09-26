# Task: Write a function ‘exists’ which takes a variable symbol v and returns whether v is defined

def exists():

    # takes in any input
    v = input("Enter the variable to check: ")

    # check if given input is defined globally
    return v in globals()