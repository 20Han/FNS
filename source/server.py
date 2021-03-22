import socket
import time

HOST = '127.0.0.1'
PORT = 30000
BUFSIZE = 1024
ADDR = (HOST, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
  serverSocket.bind(ADDR)
  serverSocket.listen()

  while True:
    clientSocket, clientAddr = serverSocket.accept()
    print(clientAddr)
    result = ''

    while True:
      data = clientSocket.recv(BUFSIZE)
      if not data:
        break
      result += data.decode()
    
    print(result)
    with open('data_{}'.format(time.time()), 'w') as f:
      f.write(result)
    clientSocket.close()