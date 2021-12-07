# Filename: m2p2.py
# Author: Jack Chen
# Course: ITSC203
# Details: Prints details about the contents of the specified directory

import sys, os, time

directory = os.chdir(sys.argv[1])                                                           #retrieves and sets the directory to be searched from the commandline

with os.scandir(directory) as entries:                                                      #ensures that the resource opened will be closed properly once it is completed, regardless of how
    for entry in entries:
        if os.path.isfile(entry.name):                                                      #if the name is a file, then print
            absolute_path = os.path.abspath(entry.name)                                     #creates the absolute path for the file name to be used later               
            print('File Name\t: ' + entry.name)                                             #print file name
            print('File Path\t: ' + absolute_path)                                          #print absolute path                                  
            print('File Size\t:',os.path.getsize(absolute_path), 'bytes')                   #print file size
            print('Inode    \t:', entry.inode())                                            #print inode
            print('Last Mod \t:', time.ctime(os.path.getmtime(entry.name)),'\n')            #print last modification date
