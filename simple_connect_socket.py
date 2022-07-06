import socket
import time
import struct


HOST = '127.0.0.1'
PORT = 1337

def p32(i:int)->bytes:
	return struct.pack('<I', i)

def p64(i:int)->bytes:
	return struct.pack('<Q', i)

def u32(b:bytes)->int:
	return struct.unpack('<I', b)

def u64(b:bytes)->int:
	return struct.unpack('<Q', b)


class Connect:
	def __init__(self, host:str, port:int):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((host, port))

	def send_bytes(self, b:str)->bytes:
		self.s.send(str(b).encode() + b'\n')
		rep = self.s.recv(1024)
		return rep

	def recv(self, size:int)->bytes:
		return self.s.recv(size)

	def recv_until(self, patern:str)->bytes:
		patern = patern.encode()
		rep = b''
		while patern not in rep:
			rep += self.s.recv(1024)
			# stop condition
			if b'FLAG' in rep:
				return rep
		return rep

	def close(self):
		self.s.close()


def main():
	s = Connect(HOST, PORT)
	s.send_bytes("hello")



if __name__ == "__main__":
    main()
