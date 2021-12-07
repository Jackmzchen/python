from ctypes import *

class struct(Structure):
    _fields_ = [ 
        ('name', (c_char * 30)),
        ('studentID', c_int),
        ('classes', (c_char * 30)),
        ('scores', (c_int * 30)),
        ('scores2', (c_float * 30))
    ]

Jack = struct(b"Jack", 5622486, b"ITSC203",(10, 20, 60, 70, 80))            #passes values to the struct created in the previous question
name = ((c_char * 30)(*b'Jack'))                                            #defines name as a char array of 30 and iniitalizes it with my name
classes = ((c_char * 30)(*b'ITSC203'))                                      #defines classes as a char array of 30 and iniitalizes it with the class
studentID = (c_int)(5622486)                                                #defines studentID as a int and iniitalizes it with a number
scores = (c_int * 30)(*(10, 20, 60, 70, 80))                                #defines scores as a int array of 30 and iniitalizes it with the scores
scores2 = (c_float * 30)(*(10.4, 50.6, 70.45, 80.1))                        #defines scores2 as a float array of 30 and initializes it with the float point scores

print('Name:\t\t', name.value.decode('utf-8'))                              #prints the value stored in name
print('StudentID:\t', studentID.value)                                      #prints the value stored in studentID
print('Classes:\t',classes.value.decode('utf-8'))                           #prints the value stored in classes
print('Scores:\t\t ', end = '')
for score in scores:                                                        #prints the values in scores
    if score == 0:                                                          #does not print anything if there is a 0
        break
    else:
        print(score,' ', end ='')

print('\nScores2:\t ', end = '')      
for score in scores2:                                                       #prints the values stored in scores2
    if score == 0:                                                          #does not print anything if there is a 0
        break
    else:
        print(f'%.2f' % score,' ', end ='')


