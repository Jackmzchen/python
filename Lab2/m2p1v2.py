import random, string

strings = []
seq,arch = input("Please enter seq length and architecture, seperated by a space respectively: ").split()
if int(seq) >= 5 and int(seq) <= 1024 and (int(arch) == 4 or int(arch) == 8):
    print('Your generated sequence of length ' + seq + ' is:')
    for l in range(int(seq)):                                                                                               #sequence length
        for n in range(int(arch)):                                                                                          #byte size architecture
            strings.append(string.ascii_uppercase[l] + string.digits[n] + string.ascii_lowercase[l+1]+string.digits[n])
            fullstr = ''.join(strings)
    print(fullstr)
else:
    print('The length you entered was below the minimum allowed(100) or the architecture is not 4 or 8')
print()
substring = input('Please enter a substring: ')
result = fullstr.find(substring)
if result != -1:
    print('Sub-sequence was found at offset: ', result)
    print('Your pattern ',substring + ' was not found anywhere else')
else:
    print('sub-sequence is not found')