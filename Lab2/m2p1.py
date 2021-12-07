# Filename: m2p1.py
# Author: Jack Chen
# Course: ITSC203
# Details: Prints a random sequence of 4 or 8 bytes

import random, string

final = ''

seq,arch = input("Please enter seq length and architecture, seperated by a space respectively: ").split()
if int(seq) >= 100 and int(seq) <= 1024 and (int(arch) == 4 or int(arch) == 8):                                                                 #determines if the correct entries are entered by the user
    print('Your generated sequence of length ' + seq + ' is:')
    for x in range(int(int(seq)/int(arch))):                                                                                                    #gets the actual character length to print when divided by 4 or 8
        strings = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k= (int(arch))))                      #creates the group of 4 character sequences or 8 character sequences
        final += strings                                                                                                                        #joins the sequences together to form one string
    print(final)                                                                                                                                #prints the final string
else:
    print('The length you entered was below the minimum allowed(100) or the architecture is not 4 or 8')
print()
substring = input('Please enter a substring: ')

result = final.find(substring)                                                                                                                  #find the substring in the string
count = final.count(substring)                                                                                                                  #count how many times the substring is in the string
if result != -1:
    print('Sub-sequence was found at offset:', result)
    print('Substring was found ', count, ' times')
else:
    print('sub-sequence is not found')