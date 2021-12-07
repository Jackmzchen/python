
lst = []
with open('profile.txt','r') as file:
    lst = file.readline().split(' ')
    lst.sort()
    lst = set(lst)
    for x in lst:
        print(x.replace(':','->').replace('_', ' '))
