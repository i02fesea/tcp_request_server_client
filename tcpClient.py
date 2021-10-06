import json
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

jsonResult = {"area": "56","year": "1992","rooms": "5","bedrooms": "2","balcony": "no"}
jsonResult = json.dumps(jsonResult)

try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # socket = socket.socket()
except socket.error as err:
    print('Socket error because of %s' %(err))

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
socket.connect((HOST, PORT))
socket.sendall(bytes(jsonResult,encoding="utf-8"))


# Receive data from the server and shut down
received = socket.recv(1024)
jsonReceived = received.decode("utf-8")

print("Json received -->", jsonReceived)

socket.close()

    # s.connect((HOST, PORT))
    # s.sendall(b'Hello, world')
# socket.send(jsonResult)
# data = socket.recv(1024)

print('Received', repr(received))