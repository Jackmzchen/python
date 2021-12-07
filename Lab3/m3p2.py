#!/usr/bin/python3
# Filename: m3p1.py
# Author: Jack Chen 
# Course: ITSC203
# Details: tries to crack the password of the accounts listed in the program

import pexpect
from itertools import permutations
from string import ascii_letters

def resultcheck(child):                                                                                                     #checks the result of the message after sending the password

    goodpasswd = False
    fail = ['You got in to the wrong part of the program','Please try again','Mission scrubbed!!!',"Don't feel bad",'Congratulations, you get to try again!!!']
    child.expect('\t')
    result = child.buffer.decode('utf-8').replace('\r\n','')                                                                #places the result after passing in the password to see if it matches one of the fail messages
    
    if result in fail:
            print('Access Message: ', result)                                                                              #print the result message if it fails
            return goodpasswd
    else:
        print('Successful Access Message: ', result)                                                                          
        goodpasswd = True
        return goodpasswd

def passwdguess(chars, maxlength):
    return(''.join(guess) for passwdlength in range(5, maxlength+1) for guess in permutations(chars, passwdlength))        #generates the passwords to check

if __name__ == '__main__':
    
    for potentialpasswd in passwdguess(ascii_letters,10):
        usernames = set() ; jtru_passwd = set() ; rbg_passwd = set() ; bob_passwd = set()
        offset = 0 ; passwd = '' ; attempt = 0 ; jtru = False ; rbg = False ; bob = False

        for letter in potentialpasswd:                                                                                     #converts the generated password into the one created by the algorithm
            passwd += chr((ord(letter) ^ 0x22) * (len(potentialpasswd) - offset))
            offset += 1
        print('The converted password is: ', passwd)

        while attempt < 40:                                                                                                #spawns the programs 40 times to capture all the users and ensure that each user has been attempted once with the password
            child = pexpect.spawn('./strange')
            child.expect('password:')
            user = child.before.decode('utf-8').replace("'s",'')[13:]
            usernames.add(user)                                                                                            #keep track of the usernames that has appeared
    
            if 'jtrudeau' in user and jtru == False:
                jtru = True                                                                                                #ensures that jtru only runs once
                print("\nTrying to access jtrudeau's account")
                child.sendline(passwd)
                goodpasswd = resultcheck(child)
                if goodpasswd == True:
                    jtru_passwd.add(passwd)
                                                                                                               
            if 'rbginsburg' in user and rbg == False:
                rbg = True                                                                                                 #ensures that rgb only runs once
                print("\nTrying to access rbginsburg's account")
                child.sendline(passwd)
                goodpasswd = resultcheck(child)
                if goodpasswd == True:
                    rbg_passwd.add(passwd)
                                                                                                                 

            if 'bobama' in user and bob == False:
                bob = True                                                                                                 #ensure that bob only runs once
                print("\nTrying to access bobama's account")
                child.sendline(passwd)
                goodpasswd = resultcheck(child)
                if goodpasswd == True:
                    bob_passwd.add(passwd)

            if jtru == True and rbg == True and bob == True:                                                               #stops the attempt once all the users have ran once 
                print('\nCurrent password does not work... Resetting for next password guess\n')
                break
            attempt += 1

print('There is', len(usernames), 'users avaliable to login as in the program\nThe usernames are:')                        #prints the usernames and how many there is
for x in usernames:
    print(x)
    
for x in usernames:
    print("The successful passwords for ", x,'is:')                                                                         #prints successful passwords for each of the users
        
    if 'jtrudeau' in x:
         for x in jtru_passwd:
            print(x)
    if 'rbginsburg' in x:
        for x in rbg_passwd:
            print(x)
    if 'bobama' in x:
        for x in bob_passwd:
            print(x)
