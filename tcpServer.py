import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

sock = socket.socket()
print("Socket created ...")

sock.bind((HOST, PORT))
sock.listen(5)

print('socket is listening')

while True:
    c, addr = sock.accept()
    # print 'got connection from ', addr

    received = c.recv(1024)

    jsonReceived = received.decode("utf-8")
    print("Json received -->", jsonReceived)

    c.sendall(received)

    c.close()

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print('Connected by', addr)
#         while True:
#             # data = conn.recv(1024)
#             data = conn.recv(1024)
#             print("Json received -->", data)
#             if not data:
#                 break
#             conn.sendall(data)