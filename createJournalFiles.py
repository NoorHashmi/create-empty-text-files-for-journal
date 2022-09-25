import os

def promptUserToInputDetailsAndPerformAction():
    firstYear = int(input('Enter first year (in 2022 format)'))
    lastYear = int(input('Enter last year in (in 2022 format)'))
    years = list(range(firstYear, lastYear+1))
    print('years: ', years)

    firstMonth = int(input('Enter first month'))
    lastMonth = int(input('Enter last month'))
    months = list(range(firstMonth, lastMonth+1))
    print('Months: ', months)

    firstDay = int(input('Enter first day'))
    lastDay = int(input('Enter Last day'))
    days = list(range(firstDay, lastDay+1))
    print('Days: ', days)

    action = input('create files or delete files ? ')

    createOrDeleteJournalFiles(action, years, months, days)

def createOrDeleteJournalFiles(action = 'none' , years = [2022], months = list(range(1,13)), days = list(range(1, 32))):
    if (action != 'create' and action != 'delete'):
        print('\n Please specify if you want to create or delete files.\n')
        return()

    for month in months:
        if (monthIsInvalid(month)):
            print('month cannot be ', month)
            print('Please enter a list of months ranging from 1 to 12\n')
            return()

    for day in days:
        if(dayIsInvalid(day)):
            print('day cannot be ', day)
            print('Please enter a list of days ranging from 1 to 31\n')
            return()




    isLeapYear = False
    superMonths = [1, 3, 5, 7, 8, 10, 12]
    isSuperMonth = False


    for year  in years:
        if (year%4 == 0):
            isLeapYear = True
        else:
            isLeapYear = False

        stringYear = str(year)

        for month in months:
            if (month in superMonths):
                isSuperMonth = True

            else:
                isSuperMonth = False

            if (month == 2):

                if (isLeapYear):
                    maxDays = 29
                else:
                    maxDays = 28
            else:
                if(month in superMonths):

                    maxDays = 31
                else:

                    maxDays = 30

            if(month <= 9):
                stringMonth = '0' + str(month)
            else:
                stringMonth = str(month)

            for day in days:
                if (day < 1 or day > maxDays):
                    continue

                if(day <= 9):
                    stringDay = '0' + str(day)
                else:
                    stringDay = str(day)


                fileName = 'journalFiles/' + stringYear + '-' + stringMonth + '-' + stringDay + '_'  + 'JournalEntry.txt'

                if(action == 'create'):
                    createFile(fileName)
                if(action == 'delete'):
                    deleteFile(fileName)

def createFile(fileName):
    if (os.path.exists(fileName)):
        print('File "', fileName, '" already exists.')
        return()
    else:
        file = open(fileName, 'w')
        file.close()
        print('File "', fileName,'" created successfully.')
        return()

def deleteFile(fileName):
    if os.path.exists(fileName):
        os.remove(fileName)
        print('The file "', fileName, '" deleted sucessfully.')
    else:
        print('The file "', fileName, '" does not exist')
    return()

def monthIsInvalid(month):
    if (month in list(range(1, 13))):
        return(False)
    else:
        return(True)

def dayIsInvalid(day):
    if (day in list(range(1, 32))):
        return(False)
    else:
        return(True)

if __name__ == '__main__':

    years = [2022]
    months = [9, 10, 11, 12]
    days = [1,2,3,4,5]
    createOrDeleteJournalFiles(action = 'create', years = years, months = months)
    
