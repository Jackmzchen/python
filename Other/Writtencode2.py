
def outMemInfo(usrinput):
    # This code prints the first 5 lines above
    with open(usrinput,'r') as file:
        fd = file.readlines()
        for items in fd:
            print(items,end = '')

def main():
    # Ask for the name of the file here
    usrinput = input('Please enter the name of the file: ')
    if not '.txt' in usrinput:
        usrinput = usrinput + '.txt'
    outMemInfo(usrinput)

if __name__ == '__main__':
    main()