# Filename: m1p3.py
# Author: Jack Chen
# Course: ITSC203
# Details: Prints details about the notepad.exe through looking at the PEfile

import datetime,time,pefile

name = input("Please enter your name: ")                                                
currenttime = datetime.datetime.now()                                                                       #retrieves the current time

file_name = input('Please enter an .exe file name: ')
if file_name.find('.exe') == -1:                                                                            #looks at the entry of the exe file name, if .exe does not exist then it is appended
    file_name = ''.join(file_name + '.exe')

print('\nReport generated by:',name)                                                                        #report generated by
print('Contact   :', name.split()[0] + '.' + name.split()[1]+ '@edu.sait.ca')                               #creates the contact info
print('Date/Time :',currenttime.strftime('%b-%d-%Y %H:%M:%S'),f'(utc: {int(time.time())})')                 #inserts the date and time

with open(file_name,'rb') as file:
    magic = file.read(2).hex().upper()                                                                      #reads the magic number, converts it to hex and uppercases the result
    file.seek(0x3C)                                                                                         #sets the pointer to the location of the PEfile Header
    peheader = file.read(1).hex().upper()                                                                   #reads the byte at the location, converts it to hex and uppercases the result
    file.seek(0xFC)                                                                                         #sets the pointer to the location that machine is located
    machine = file.read(2).hex().upper()                                                                    #reads the two bytes to give the information
    file.seek(0x120)                                                                                        #sets the pointer to the location of entry point
    entry = file.read(3).hex().upper()                                                                      #reads the 3 bytes of entry point, converts it to hex and uppercases the result
    file.close()

pe = pefile.PE(file_name)                                                                                   #opens the file with the PEfile module

print('\nManual Way:\n')
print('File Name\t\t:',file.name)
print('Magic\t\t\t:','0x'+magic[2:]+magic[:2])
print('PE Header Offset\t:','0x'+peheader)
print('Format\t\t\t:',machine[:2] + ' bit')
print('Endian\t\t\t: Big')
print('Machine\t\t\t:','0x' + machine[2:] +'-'+ machine[:2])
print('Entry Point\t\t:','0x' + entry[5:]+ entry[2:4]+entry[:2])

print('\nUsing PEfile Module:\n')
print('File Name\t\t:',file_name)
print('Magic\t\t\t:',hex(pe.DOS_HEADER.e_magic).upper().replace('X','x'))
print('PE Header Offset\t:',hex(pe.DOS_HEADER.e_lfanew).upper().replace('X','x'))
print('Endian\t\t\t: Big')
print('Format\t\t\t:',hex(pe.FILE_HEADER.Machine)[4:] + ' bit')
print('Machine\t\t\t:',hex(pe.FILE_HEADER.Machine)[:4]+'-'+hex(pe.FILE_HEADER.Machine)[4:])
print('Entry Point\t\t:',hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint).upper().replace('X','x'))