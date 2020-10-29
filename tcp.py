import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
print(ip)
#ip = "127.0.1.1"
port = 8888
address=(port)
server.bind((ip,port))
#erver.bind(address)

#figure out how to deal with that already in use error


server.listen(1)
print("started listening on",ip,":",port)
client,addr = server.accept()
print("got connection from",addr[0],":",addr[1])
while True:
	data = client.recv(1024).decode()
	print("received '",data,"' from client")
	if(data=="Helloserver"):
		client.send("Hello client".encode())
		print("reply sent")
	elif(data=="disconnect"):
		client.send("goodbye".encode())
		client.close()
		break
	else:
		client.send("invalid data".encode())
		print("invalid data")

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# address = ("127.0.1.1",41412)
# sock.bind(address)

# print([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]][:1])

# print(socket.gethostbyname(socket.gethostname()))

# while True:
#   data, addr = sock.recvfrom(1024)
#   print(data, addr)