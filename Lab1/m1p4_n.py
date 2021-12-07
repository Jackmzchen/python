#! usr/bin/python3

table = [['kenny rogers', '/home/users/KRogers'],['tony robbins','/home/TRobbins'],
[ 'johnny cash', '/home/users/JCash'],[ 'tito jackson', '/home/hut/TJackson'],
[ 'tim tzuyu', '/home/users/TTzuyu'], ['kareena kapoor', '/home/users2/KKapoor']]
lstr = [0,0]

for length in table:
    if len(length[0]) > lstr[0]:
        lstr[0] = len(length[0])
    if len(length[1]) > lstr[1]:
        lstr[1] = len(length[1])
print('+----------------+-----------------------+')
for i in table:
    col_1 = lstr[0]-len(i[0])
    col_2 = lstr[1]-len(i[1])
    print('| '+i[0].title()+' '*col_1+' | '+i[1]+' '*col_2+'  |')
print('+----------------+-----------------------+')
