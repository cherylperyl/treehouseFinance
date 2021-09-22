# Task: What is the average salary of employees who do not manage anyone? 
# In the sample above, that would be John, Mike, Joe and Dan, since they do not have anyone reporting to them

from q1a_code import extractData

# 1 - find set of manger ids
def extractMID(filename):
    data = set()
    with open(filename) as f:
        for line in f:

            # collect data excluding header
            if 'id' not in line:
                line = line.rstrip('\n')
                columns = line.split('\t')

                # add mIDs to set
                if columns[3] != 'NULL':
                    data.add(columns[3])

    return data

# 2 - for each employee, if not in set of mIDs, add salary to total, then get average
def averageSalaryOfNonManagers(filename):
    managers = extractMID(filename)
    employees = extractData(filename)

    salaries = []

    # for each employee
    for eid, info in employees.items():

        # if employee not a manager, append salary to list
        if eid not in managers:
            salaries.append(float(info[1]))
    
    # return average salary (total/count)
    return sum(salaries)/len(salaries)
