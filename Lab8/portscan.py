from socket import *

ip = input("Please Enter an IP: ")
port = int(input("Please enter the starting port: "))

failed = 0
with open("sucessful_ip_addresses.txt", "a") as file:
    successports = open("Open_ports.txt", "a")
    while port < 65535:
        mysock = socket(AF_INET,  SOCK_STREAM)
        success = mysock.connect_ex((ip, port))
        if success == 0:
            print("Connection to %s on port: %d is successful" % (ip, port))
            file.write("Connection to %s on port: %d is successful\n" % (ip, port))
            successports.write("%d\n" % port)
        else:
            failed += 1
        port += 1
successports.close()
print("%d ports are either closed or not accessible" % failed)    