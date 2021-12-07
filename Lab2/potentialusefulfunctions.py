import random, string

str = []
str = [x for l in str for x in l]           #flattens the nested list into a regular list
u = string.ascii_uppercase                  #prints A to Z in uppercase     need the string module
l = string.ascii_lowercase                  #prints a to z in lowercase     need the string module
n = string.digits                           #prints 0 to 9                  need the string module

print(f'{"put a variable name in here"}')   #for formating strings

print(u)
print(l)
print(n)
