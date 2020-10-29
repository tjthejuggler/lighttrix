from socket import *
import struct

data = struct.pack("!BB", 0x10, 4)
udp_header = struct.pack("!bIBH", 66, 0, 0, 0)
s = socket(AF_INET, SOCK_DGRAM)
s.sendto(udp_header+data, ('192.168.43.85', 41412));
