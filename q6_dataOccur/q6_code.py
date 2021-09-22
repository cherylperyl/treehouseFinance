# In a text file, give me total number of appearance of “date” within the text file 
# The date format can appears in either one (or multiple) formats shown below:
# a. YYYY/MM/DD
# b. MM/DD/YYYY
# c. DD/MM/YYYY
# d. DD (Jan/Feb/Mar/Apr/May/Jun/Jul/Aug/Sept/Oct/Nov/Dec) YYYY


import datetime

def totalDate(f):

    count = 0

    with open(f) as f:
        for line in f:
            line = line.rstrip('\n')

            if len(line)>9:
                date = line[0:10].split('/')

                if len(date) == 3:

                    # a. YYYY/MM/DD
                    if checkNumDate(date[0],date[1],date[2]):
                        count += 1

                    # b. MM/DD/YYYY
                    elif checkNumDate(date[2],date[0],date[1]):
                        count += 1
                    
                    # c. DD/MM/YYYY
                    elif checkNumDate(date[2],date[1],date[0]):
                        count += 1
                
                # d. DD (Jan/Feb/Mar/Apr/May/Jun/Jul/Aug/Sept/Oct/Nov/Dec) YYYY
                else:
                    date = line[0:12].split(' ')
                    if checkD(date):
                        count += 1

    return count

# function to check if year, month, day combi is valid
def checkNumDate(year,month,day):
    isValidDate = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False
    
    return isValidDate

# function to specifically check for case D since need to convert month to a number
def checkD(date):
    day, month, year = date[0],date[1],date[2]

    try:
        datetime_object = datetime.datetime.strptime(month, "%b")
        month = datetime_object.month
    except ValueError:
        isValidDate = False

    isValidDate = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False
    
    return isValidDate
