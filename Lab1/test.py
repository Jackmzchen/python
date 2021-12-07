

table = [""]


for i in names:
    print(i, " \t", end = '')
    if len(i.split()) > 1:
        print(i.split()[0] + "." + i.split()[1] + "@sait.ca \t", list(i)[0] + i.split()[1] + "@sait.ca")
    else:
        print(i + "@sait.ca  \t", i + "@sait.ca")
