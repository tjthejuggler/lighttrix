import subprocess 

#for pingFirst in range(0,255):
pingFirst = 43
for pingSecond in range(240,255,5): 
	address = "192.168."+ str(pingFirst) +"." + str(pingSecond) 
	res = subprocess.call(['ping', '-c', '3', address]) 
	print(str(res))
	if res == 0: 
		print( "!!!!!!!!!!!!!!ping to", address, "OK") 
	elif res == 2: 
		print("no response from", address) 
	else: 
		print("ping to", address, "failed!") 

		#a higher level async thing may be a lot easier to work with
		#look into asyncio (module?)
		#https://github.com/python-trio/trio/issues/537#issuecomment-390499367

		#i remember doing something with scapy, `pkt = IP(..) / UDP() / data`
		#struct.pack("!BB", 0x10, 4)
		#in struct.pack()
		#char, uint32, uint8, unit16 = "bIBH"

		#make one of them connect to a common wifi the computer connect to, and just listen on that iface ?
