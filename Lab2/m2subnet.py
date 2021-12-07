# Filename: m2subnet.py
# Author: Jack Chen
# Course: ITSC203
# Details: Prints the the two requested IP addess and their respective range

ip,subnet = input('Enter ip address and subnet(has to be 26): ').split()
print()

address= [] ; x = 0 
next= int(ip[8:9])
max = next + 2

while next < max:
    while x < 64:
        address.append(ip[:8] + str(next) +'.' + str(int(ip[10:])+x))
        x +=1
    print('Subnet Network Address   :',address[0] + '/'+subnet)
    print('Subnet First Address     :',address[1] + '/'+subnet)
    print('Subnet Last Address      :',address[62] +'/'+subnet)
    print('Subnet Broadcast Address :',address[63] + '/'+subnet)
    print('Range of IP Address      :',address[1] + ' to ' + address[62],'\n')
    next +=1
    x = 0
    address.clear()
