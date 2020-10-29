#!/usr/bin/env python

import socket



sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ("192.168.43.240",41412)
sock.bind(address)

print([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]][:1])

print(socket.gethostbyname(socket.gethostname()))

while True:
  data, addr = sock.recvfrom(1024)
  print(data, addr)