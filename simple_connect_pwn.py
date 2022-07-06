#!/usr/bin/env python3

from pwn import *

HOST = "chall.host.com"
PORT = 1337

def main():
    r = remote(HOST, PORT)
    r.send()
    r.sendline()
    r.recv()
    r.recvuntil()


if __name__ == "__main__":
    main()
