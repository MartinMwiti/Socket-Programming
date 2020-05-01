import socket

HEADER = 1024
PORT = 9090
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DICONNECT"
SERVER = socket.gethostbyname(socket.gethostname())   # "192.168.99.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length.encode(FORMAT))
    send_length += b''*(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(1024).decode(FORMAT)) # Receice message from the server

send("Hello there!")
send(DISCONNECT_MESSAGE)
