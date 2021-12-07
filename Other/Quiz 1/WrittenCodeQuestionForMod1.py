#! usr/bin/python3

#names are split into two lines so that it is easier to read
names = [["Luke Cage","Luke.Cage@sait.ca","LCage@sait.ca"],["Burt Reynolds","Burt.Reynolds@sait.ca","BReynolds@sait.ca"],
["Halsey","Halsey@sait.ca","Halsey@sait.ca"],["The_Weekend","The_Weekend@sait.ca","The_Weekend@sait.ca"]]

longstring = [0, 0, 0]

for length in names:                                #calculate the length of each section in the list
    if len(length[0]) > longstring[0]:              #if the length is greater than the value in longstring[0] replace that value
        longstring[0] = len(length[0])
    if len(length[1]) > longstring[1]:              #if the length is greater than the value in longstring[1] replace that value
        longstring[1] = len(length[1])
    if len(length[2]) > longstring[2]:              #if the length is greater than the value in longstring[2] replace that value
        longstring[2] = len(length[2])

for i in names:
    print(i[0]+' '*(longstring[0]-len(i[0]))+' '+i[1]+' '*(longstring[1]-len(i[1]))+' '+i[2])
