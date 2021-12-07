#!/usr/bin/python3
import os

class LinuxProcess:
    def __init__(self, pid):                                                                            #sets the pid to be used to open the correct file
        self.pid = pid

    def getInfo(self):                                                                                  #gets the info from the stat file related to the pid
        with open(os.path.join('/proc', str(self.pid),'stat'), 'r') as file:
            for x in file:
               lst = x.split(' ')                                                                       #stores the values in a list starting at the index of 0
        return lst
    
    def printData(self, lst):                                                                           #prints the info pulled from the stat file and right aligns it
        rjustwidth = 12
        startwidth = 13
        print('Name:'.rjust(startwidth),'\t', lst[1][1:].replace(')', ''),'\n','PID:'.rjust(rjustwidth),'\t', lst[0],'\n','PPID:'.rjust(rjustwidth),'\t', lst[3])
        print('RSS:'.rjust(startwidth),'\t', hex(int(lst[23])),'\n','RSSLIM:'.rjust(rjustwidth),'\t', hex(int(lst[24])),'\n','Start_Code:'.rjust(rjustwidth),'\t', hex(int(lst[25])))
        print('End_Code:'.rjust(startwidth),'\t', hex(int(lst[26])),'\n','Start_Stack:'.rjust(rjustwidth),'\t', hex(int(lst[27])),'\n','Start_Data:'.rjust(rjustwidth), '\t', hex(int(lst[44])))
        print('End_Data:'.rjust(startwidth),'\t', hex(int(lst[45])),'\n','Start_Brk:'.rjust(rjustwidth),'\t', hex(int(lst[46])),'\n','Arg_Start:'.rjust(rjustwidth), '\t', hex(int(lst[47])))
        print('Arg_End:'.rjust(startwidth),'\t', hex(int(lst[48])),'\n','Env_Start:'.rjust(rjustwidth), '\t', hex(int(lst[49])),'\n','Env_End:'.rjust(rjustwidth),'\t', hex(int(lst[50])))

def call_process(pid):                                                                                  #calls the class and gets the data
    process = LinuxProcess(pid)
    prc = process.getInfo()
    process.printData(prc)

if __name__ == '__main__':
    choice = int(input('Please enter 1 to enter the PID to analyze or enter 2 to get info on the current program\n'))

    if choice == 1:
        pid = int(input('Please enter the PID you would like to analyze: '))
        call_process(pid)
    elif choice == 2:
        call_process(os.getpid())
    else:
        print('You did not enter 1 or 2, program exiting....')
        exit(-1)

'''
fields to pull from the stat file
1 - pid  - lst positon 0
2 - name - lst position 1
4 - ppid - lst position 3
24 - rss - lst position 23
25 - rsslim - lst position 24
26 - start code - lst position 25
27 - end code - lst position 26
28 - start stack - lst position 27
45 - start data - lst position 44
46 - end data - lst position 45
47 - start brk - lst position 46
48 - arg start - lst position 47
49 - arg end - lst positon 48
50 - env start - lst position 49
51 - env end - lst position 50
'''