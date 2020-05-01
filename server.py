import socket
import threading

PORT = 5050 # you can choose a different PORT preferably above 4000.

#SERVER = "192.168.99.1" # IPv4 Address from "ipconfig" command

SERVER = socket.gethostbyname(socket.gethostname())

# gethostbyname — Get the IPv4 address corresponding to a given Internet host name
# gethostname() gets the standard host name for the local machine. i.e the Name representing your computer in a network

# print(socket.gethostname())
# print(SERVER) # prints out your local machine IPv4 address.

ADDR = (SERVER, PORT)

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # CREATE A SOCKET
    print("Socket successfully created")
except socket.error as err:
    print (f"socket creation failed with error {err}")

# AF_INET: is an address family/category that is used to designate the type of addresses that your socket can communicate with (in this case, Internet Protocol v4 addresses). When you create a socket, you have to specify its address family, and then you can only use addresses of that type with the socket.
# SOCK_STREAM means that it is a TCP socket


server.bind(ADDR) # Bind the created socket to the 'ADDR': ADDRESS
print(f'Socket binded to {ADDR}')


def handle_client(conn, addr):
    pass



def start():
    server.listen()
    print ("socket is listening")
    while True:
        conn, addr = server.accept()
        # 'conn' is a socket object that will allow you to communicate back to the connection. 'addr' contains the information about the connection i.e addr returns the IP and PORT the connection is comming from.
        print('Got connection from', addr)
        thread = threading.Thread(target=handle_client, args=(conn, addr))




print('[STARTING] server is starting...')
start()

