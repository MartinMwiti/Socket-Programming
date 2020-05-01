import socket
import threading

HEADER = 1024
PORT = 9090 # you can choose a different PORT preferably above 4000.

#SERVER = "192.168.99.1" # IPv4 Address from "ipconfig" command

SERVER = socket.gethostbyname(socket.gethostname())

# gethostbyname — Get the IPv4 address corresponding to a given Internet host name
# gethostname() gets the standard host name for the local machine. i.e the Name representing your computer in a network

# print(socket.gethostname())
# print(SERVER) # prints out your local machine IPv4 address.

ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DICONNECT"

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # CREATE A SOCKET
    print("Socket successfully created")
except socket.error as err:
    print (f"Socket creation failed with error {err}")

# AF_INET: is an address family/category that is used to designate the type of addresses that your socket can communicate with (in this case, Internet Protocol v4 addresses). When you create a socket, you have to specify its address family, and then you can only use addresses of that type with the socket.
# SOCK_STREAM means that it is a TCP socket


server.bind(ADDR) # Bind the created socket to the 'ADDR': ADDRESS
print(f'Socket binded to {ADDR}')


def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.') # who connected
    
    connected = True
    while connected:
        # receive data/message from the client
        msg_length = conn.recv(HEADER).decode(FORMAT) # decode the message from its bytes format to string format
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False # you can replace with break if you want. Same result
                # break

            print (f"[{addr}] {msg}") # print the address of a client and the message they sent.
            conn.send("Msg received".encode(FORMAT)) # sending message to the client

        conn.close()  # close the connection



def start():
    server.listen()
    print ("[LISTENING] Server is listening on {SERVER}")

    while True:
        conn, addr = server.accept()
        # 'conn' is a socket object that will allow you to communicate back to the connection. 'addr' contains the information about the connection i.e addr returns the IP and PORT the connection is comming from.
        print('Got connection from', addr)
        thread = threading.Thread(target=handle_client, args=(conn, addr)) # target refers to handle_client func and args handles the arguments you're passing to the func whenever a new connection occurs.
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.activeCount() -1}") # print active connections i.e the number of thread in this python process. The number of threads will represent the number of clients connected. We deduct one because there is always one thread running i.e the start() func.



print('[STARTING] Server is starting...')
start()

