#!/usr/bin/env python3

from pwn import *

HOST = "chall.host.com"
PORT = 1337

def conn():
    if args.REMOTE:
        r = remote(HOST, PORT)
    else:
        r = process([exe.path])

    return r



def main():
    global r
    r = conn()
    r.send()
    r.recv()
    r.recvuntil()


if __name__ == "__main__":
    main()
