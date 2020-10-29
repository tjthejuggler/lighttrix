import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ("127.0.0.1",5002)
sock.sendto("myString".encode(),address)