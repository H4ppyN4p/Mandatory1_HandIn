#
#Assignment 1

BoardOfDirectors = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}
Management = {'Tine', 'Trunte', 'Rane'}
Employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

print('Assignment 1:')
def Assignment1():

    print('who in the board of directors is not an employee?')
    print(BoardOfDirectors - Employees )
    print('\n')

    print('who in the board of directors is also an employee?')
    print(BoardOfDirectors & Employees)
    print('\n')

    print('how many of the management is also member of the board?')
    print(len(BoardOfDirectors & Employees))
    print('\n')

    print('Are all members of the managent also an employee?')
    print(len(Management) == len(Management & Employees))
    print('\n')

    print('Are all members of the management also in the board?')
    print(len(Management) == len(Management & BoardOfDirectors))
    print('\n')

    print('Who is an employee, member of the management, and a member of the board?')
    print(BoardOfDirectors & Management & Employees)
    print('\n')

    print('Who of the employee is neither a memeber or the board or management?')
    print(Employees - BoardOfDirectors - Management)
    print('\n')

Assignment1()
print('\n'*2)

#
#Assignment 2
data = {'a': 'Alpha', 'b' : 'Beta', 'g': 'Gamma'}

listOfTuples = []

print('Assignment 2:')
def Assignment2():
    for val in data:
        keyValue = {val, data[val]}
        listOfTuples.append(tuple(keyValue))

    print('List of Tuples:')
    print(listOfTuples)    
    print('\n')

Assignment2()
print('\n'*2)

#
#Assignment 3
set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

print('Assignment 3:')
def Assignment3():
    #Set Methods:
    #Union Set Methods:
    unionSetMethods = set1.union(set2)
    print('Union Set Methods:')
    print(unionSetMethods)
    print('\n')

    #Symmetric Difference Set Methods:
    symDifferenceSetMethods = set1.symmetric_difference(set2)
    print('Symmetric Difference Set Methods:')
    print(symDifferenceSetMethods)
    print('\n')

    #Difference Set Methods:
    differenceSetMethods = set1.difference(set2)
    print('Difference Set Methods:')
    print(differenceSetMethods)
    print('\n')

    #Disjoint Set Methods:
    disjointSetMethods = set1.intersection(set2)
    print('Disjoint Set Methods:')
    print(disjointSetMethods)
    print('\n')

    #Set Operators:
    #Union Set operators:
    unionSetOperators = (set1 | set2)
    print('Union Set Operators:')
    print(unionSetOperators)
    print('\n')

    #Symmetric Difference Set Operators:
    symmeetricDifferenceSetOperators = (set1 ^ set2)
    print('Symmetric Difference Set Operators:')
    print(symDifferenceSetMethods)
    print('\n')

    #Difference Set Operators:
    differenceSetOperators = (set1 - set2)
    print('Difference Set Operators:')
    print(differenceSetOperators)
    print('\n')

    #Disjoint Set Operators:
    disjointSetOperators = (set1 & set2)
    print('Disjoint Set Operators:')
    print(disjointSetOperators)
    print('\n')

Assignment3()
print('\n'*2)

#
#Assignment 4
exampleStringToDecode = '8-MAR-85'

monthDict = {
    'JAN': '01',
    'FEB': '02',
    'MAR': '03',
    'APR': '04',
    'MAY': '05',
    'JUN': '06',
    'JUL': '07',
    'AUG': '08',
    'SEP': '09',
    'OCT': '10',
    'NOV': '11',
    'DEC': '12'
}

print('Assignment 4:')
def Assignment4():
    splitString = exampleStringToDecode.split('-')
    print(splitString)

    def YearMonthDay(val):
        splitVal = val.split('-')
        full_year = '19' + splitVal[2]
        month_as_numb = monthDict[splitVal[1]]

        newYeMoDa = (full_year, month_as_numb, splitVal[0])
        return newYeMoDa


    print(YearMonthDay(exampleStringToDecode))

Assignment4()
print('\n'*2)

#
#Assignment 5:
friendsInvited = ['James', 'Jones', 'Anna', 'Bettany', 'Kenneth', 'Olivia']
friendsRSVP = ['Jones', 'Hanna', 'Lianne', 'Bettany', 'Lars', 'Peter', 'Benjamin', 'Olivia']

print('Assignment 5:')
def Assignment5(invited, RSVP):
    didRSVP = []
    noRSVP = []
    RSVPbutNoInv = []
    for friend in invited:
        for otherFriend in RSVP:
            if friend == otherFriend:
                didRSVP.append(friend)

    for friend in invited:
        if didRSVP.count(friend) == 0:
            noRSVP.append(friend)

    for friend in friendsRSVP:
         if didRSVP.count(friend) == 0:
            RSVPbutNoInv.append(friend)

    print('invited and RSVPed:')
    print(didRSVP)
    print('\n')

    print('invited but did not RSVP:')
    print(noRSVP)
    print('\n')

    print('Not invited but RSVPed:')
    print(RSVPbutNoInv)
    print('\n')

Assignment5(friendsInvited, friendsRSVP)
print('\n'*2)

#
#OPS! Takes User Input
#Assignment 6:
gradesDict = {
'Ganizani' : '80',
'Timon' : '80',
'Ladislas' : '90',
'Tanvi' : '90',
'Georgianna' : '90',
'Ernest' : '80',
'Sonja' : '80',
'Sedna' : '90',
'Mowgli' : '80',
'Musa' : '90',
'Cyra' : '80',
'Natanail' : '90'
}

studentsToUpdate = ['Timon', 'Tanvi', 'Sedna', 'Max']

print('Assignment 6:')
def Assignment6(listOfStudents):
    for student in listOfStudents:
        if student in gradesDict:
            print('Choose ' + student + '-s new grade')
            newGrade = input()

            gradesDict[student] = newGrade

    for student in gradesDict:
        if int(gradesDict[student]) >= 85:
            print(student + ' their grade is: ' + gradesDict[student])  

Assignment6(studentsToUpdate)
print('\n'*2)