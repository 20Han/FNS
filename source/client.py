import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 30000
BUFSIZE = 1024
SERVER_ADDR = (SERVER_IP, SERVER_PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
  clientSocket.connect(SERVER_ADDR)
  clientSocket.send('hello'.encode())