# Filename: m3p1.py
# Author: Jack Chen 
# Course: ITSC203
# Details: Prints out the table asked in the problem.

import hashlib, os
from shutil import copyfile

subdir= {}
BUFFER_SIZE = 65536                                                                             #the size of each read from the file

for x in os.listdir(os.getcwd()):
    if os.path.isdir(x):                                                                        #automatically finds the folder in the directory
        if x.find('folder') == 0:
            dir = x
path = os.getcwd() + '/filetypes'                                                               #creates a new folder to store the new folders in
if os.path.exists(path) != True:                                                                #will only create the parent folder if it does not exist already
    os.mkdir(path)                                    

file_hash = hashlib.sha512()                                                                    #creates hash object and sets it to sha512
for root, dirs, files in os.walk(dir):
        subdir[root] = files

        if subdir[root] == []:                                                                  #if the folders do not contain any files move on
            print('Parent folder:\n',root,'\n')
            print('Subfolders:')
            continue       
        else:
            values = subdir.pop(root)                                                           #retrieves the values associated with the key
            print('\n'+root[10:])
            print('Files in the folder:')
        
            for x in values:  
                print('\t'+ x)                                      
                with open(os.path.join(root,x), 'rb') as file:
                    fr = file.read(BUFFER_SIZE)
                    while len(fr) > 0:                                                          #while there is still data in fr continue reading
                        file_hash.update(fr)                                                    #updates the hash variable with the new information
                        fr = file.read(BUFFER_SIZE)
                    file.close()
                    print('\t\tFile hash is: ',file_hash.hexdigest())
                    if not os.path.exists(os.path.join(path, x[10:])):                          #makes new folders for each of the file types
                        os.mkdir(os.path.join(path, x[10:]))                                    #specifies the path of the folder
                    src = os.path.join(os.getcwd(),root + '/' + x)                              #creates the file path for the source file to copy
                    dest = os.path.join(path,x[10:],str(file_hash.hexdigest()) + x[9:])         #creates the destination file path for the file to be copied to
                    copyfile(src,dest)                                                          #copy the file to the new location