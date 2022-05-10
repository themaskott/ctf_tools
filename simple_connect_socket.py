import socket
import time
import struct

def send_bytes(s, b):
	s.send(b)
	rep = s.recv()
	return rep


HOST = '127.0.0.1'
PORT = 1337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    cookie = struct.unpack('<Q', leak)
    payload = struct.pack('<Q', ret))
