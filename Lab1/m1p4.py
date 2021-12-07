# Filename: m1p4.py
# Author: Jack Chen
# Course: ITSC203
# Details: Prints the table specified in Problem 4

name = [['kenny rogers', '/home/users/KRogers'],['tony robbins','/home/TRobbins'],
[ 'johnny cash', '/home/users/JCash'],[ 'tito jackson', '/home/hut/TJackson'],
[ 'tim tzuyu', '/home/users/TTzuyu'], ['kareena kapoor', '/home/users2/KKapoor']]

print('+-----------------+-----------------------+')
for i in name:
    if len(i[0])== 9:                                                               #looks at the length of the first element in the list if it equals 9 proceed
        print('|', i[0].title(),'      |', i[1],'   |')
    elif len(i[0]) == 11:
        print('|', i[0].title(),'    |', i[1],'    |')
    elif len(i[0]) == 12:
        if len(i[1]) == 18:
            print('|', i[0].title(),'   |', i[1],'   |')
        elif len(i[1]) == 19:
            print('|', i[0].title(),'   |', i[1],'  |')
        else:
            print('|', i[0].title(),'   |', i[1],'       |')
    else:
        print('|', i[0].title(),' |', i[1],' |')
print('+-----------------+-----------------------+')
