#Import required libraries
import socket
import threading
import time
import json

#Define a server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5555))
server.listen(100)
print("DNS Server is to ready to accept connections..")

#Data Base
data  = open('data.json', 'r')
dnsDataBase = json.load(data)

#A function to handle clients
def handleClient(cs,cadd):
    BUFSIZE = 2048
    while True:
        cs.send("Enter Domain name (Site): ".encode())
        site = cs.recv(BUFSIZE).decode()
        if site.lower() == 'exit':
            break
        if site in dnsDataBase:
            ip = dnsDataBase[site.lower()]
            msg1 = f"The Ip for {site}: >>{ip}<<\n"
            msg2 = "Query succesfully replayed at: "+ str(time.asctime(time.localtime(time.time())))
            response = msg1+msg2
            cs.send(response.encode())
        else:
            response = "Query Failed>> website not exist."
            cs.send(response.encode())

    cs.close()

def developer(cs,cadd):
    BUFSIZE = 2048
    while True:

        BUFSIZE = 2048
        cs.send("Enter New Domain name (Site): ".encode())
        site = cs.recv(BUFSIZE).decode()
        if site.lower() == 'exit':
            break
        cs.send("Enter The Correspanding IP: ".encode())
        ip = cs.recv(BUFSIZE).decode()
        dnsDataBase[site] = ip
        data = open('data.json', 'w')
        json.dump(dnsDataBase, data)

    cs.close()
#Accept clients continuously
while True:
    cs, cadd = server.accept()
    print("New client is connected>> "+cadd[0]+" :: "+str(cadd[1]))
    msg1 = "Welcome to our DNS server.\n"
    msg2 = "Enter Your State ('D' for Developer or 'U' for User): "
    msg = msg1+msg2
    cs.send(msg.encode())
    res = cs.recv(2048).decode()
    if res == 'U':
        thread = threading.Thread(target=handleClient, args=(cs,cadd))
        thread.start()
    elif res == 'D':
        thread = threading.Thread(target=developer, args=(cs, cadd))
        thread.start()
    else:
        cs.close()

# Close the Connection
server.close()
