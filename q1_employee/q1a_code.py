#Task: Give the name of employees, whose salaries are greater than their immediate manager’s

# 1 - function to extract data
# assumptions - data is in txt file, data separated by tabs, header included, data in same directory as code

def extractData(filename):
    data = {}
    with open(filename) as f:
        for line in f:

            # collect data excluding header
            if 'id' not in line:
                line = line.rstrip('\n')
                columns = line.split('\t')

                # key is eID, contents is eName, eSalary and mID
                data[columns[0]] = columns[1:]

    return data

# 2 - function to find the relevant employees
# assumption: all managers are employees too

def higherSalaryEmployees(filename):
    data = extractData(filename)

    names = []

    for eid, info in data.items():

        # if employee has no manger, pass
        if info[2] == 'NULL':
            pass

        # else check if employee salary > manager salary
        elif info[1] > data[info[2]][1]:
            names.append(info[0])

    return names

# print(higherSalaryEmployees("sampleData.txt"))