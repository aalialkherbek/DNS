import socket

#Define the address of the server
ADDRESS = ('localhost', 5555)
BUFSIZE = 2048

#Define the socket of the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)
#Recieve the state message
Msg = client.recv(BUFSIZE).decode()
res = input(Msg)

if res == 'U':
    client.send(res.encode())
    #Start DNS service
    while True:
        msg = client.recv(BUFSIZE).decode()
        res = input(msg)
        client.send(res.encode())
        if res == 'exit':
            break
        response = client.recv(BUFSIZE).decode()
        print(response)
elif res=='D':
    client.send(res.encode())
    # Start DNS service
    while True:
        msg = client.recv(BUFSIZE).decode()
        res = input(msg)
        client.send(res.encode())
        if res == 'exit':
            break
        response = client.recv(BUFSIZE).decode()
        res = input(response)
        client.send(res.encode())
#Close the connection with the server
client.close()