#!/bin/python3
# Filename: m3p1.py
# Author: Jack Chen 
# Course: ITSC203
# Details: Prints out the information in a tree format

import hashlib, os
from shutil import copyfile

def folderlocatecreate():
    
    for x in os.listdir(os.getcwd()):
        if 'folder' in x: dir = x                                                       #sets the correct directory to search   
                                       
    path = os.getcwd() + '/filetypes'                                                   #creates the new folder to store the seperate file types and the hashed files
    if os.path.exists(path) != True: os.mkdir(path)

    return path, dir

def filehash(path, dir):
    BUFFER_SIZE = 65536 ; flag = False ; subdir = {}                                    #sets the read size of each file read, a flag to False, and create a dictionary

    file_hash = hashlib.sha512()                                                        #sets the hash type to be displayed
    
    for root,dirs, files in os.walk(dir):
        subdir[root] = files                                                            #associates the directory and the files it contains

        if flag == False:                                                               #makes sure that the following line only runs once
            print('Parent folder:\n',root,'\n\n''Subfolders:') ; flag = True
                
        if subdir[root] == []: continue                                                 #if the folder dose not contain any files move on
     
        else:
            values = subdir.pop(root)                                                   #retrieves the values associated with the key in the dictonary
            print('\n'+root[10:],'\nFiles in the folder:')                              #printout the sub folders within the parent
        
            for x in values:  
                print('\t'+ x)                                      
                with open(os.path.join(root,x), 'rb') as file:
                    fr = file.read(BUFFER_SIZE)                                         #reads the file
                    while len(fr) > 0:                                                  #if there is more data to read, continue reading
                        file_hash.update(fr)                                            #updates the hash variable with the new information
                        fr = file.read(BUFFER_SIZE)                                     #reads the file until fr is 0
                    file.close()
                    print('\t\tFile hash is: ',file_hash.hexdigest())                   #print out the file hash of each file
                    
                    if not os.path.exists(os.path.join(path, x[10:])):                  #makes new folders for each of the file types
                        os.mkdir(os.path.join(path, x[10:]))                            #specifies the path of the folder

                src = os.path.join(os.getcwd(),root + '/' + x)                          #sets the source file path to copy from
                dest = os.path.join(path,x[10:],str(file_hash.hexdigest()) + x[9:])     #sets the destination file path and the name of the file
                copyfile(src,dest)                                                      #copies the file over to the new folder

if __name__ == '__main__':
    path, dir = folderlocatecreate()
    filehash(path, dir)