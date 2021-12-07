# Filename: m3p1.py
# Author: Jack Chen 
# Course: ITSC203
# Details: Prints out the table asked in the problem.

import hashlib, os
from shutil import copyfile

subdir= {}                                                                                                      #dictionary to store the subfolders and their files
BUFFER_SIZE = 65536                                                                                             #the size of each read form the file

for x in os.listdir(os.getcwd()):
    if os.path.isdir(x):                                                                                        #automatically finds the folder in the directory
        if x.find('folder') == 0:                                                                               #program finds the specified folder to look in
                dir = x

path = os.getcwd() + '/filetypes'                                                                               #program creates the folder to store the hashed file names and file types 
if os.path.exists(path) != True:
        os.mkdir(path)                                    

file_hash = hashlib.sha512()
for root,dirs, files in os.walk(dir):
        subdir[root] = files

        if flag == False:                                                                                       #makes sure that the following line only runs once
            print('Parent folder:\n',root,'\n\n''Subfolders:') ; flag = True

        else:
                values = subdir.pop(root)                                                                       #retrieves the values associated with the key
                print('\n'+root[10:])
                print('Files in the folder:')
        
                for x in values:  
                        print('\t'+ x)                                      
                        with open(os.path.join(root,x), 'rb') as file:
                                fr = file.read(BUFFER_SIZE)
                                while len(fr) > 0:                                                              #while there is still data in fr continue reading
                                        file_hash.update(fr)                                                    #updates the hash variable with the new information
                                        fr = file.read(BUFFER_SIZE)
                                        file.close()
                                print('\t\tFile hash is: ',file_hash.hexdigest())
                                if not os.path.exists(os.path.join(path, x[10:])):                              #makes new folders for each of the file types
                                        os.mkdir(os.path.join(path, x[10:]))                                    #specifies the path of the folder

                        copyfile(os.path.join(os.getcwd(),root + '/' + x),os.path.join(path,x[10:],str(file_hash.hexdigest()) + x[9:]))  