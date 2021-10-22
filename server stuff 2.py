import socket

msgFromClient = "Popa Andrei-Calin"
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("193.231.20.3", 1276)
bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
