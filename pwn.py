#!/usr/bin/env python3

from pwn import *

HOST = "chall.host.com"
PORT = 1337

exe = ELF("./file_name")

libc = ELF("/usr/lib/libc.so.6")

context.log_level = 'info'
context.arch = 'amd64'
context.binary = exe.path
context.terminal = ["tmux", "new-window"]

if args.REMOTE:
    NL = b"\r\n"
else:
    NL = b"\n"

def conn():
    if args.REMOTE:
        r = remote(HOST, PORT)
    else:
        r = process([exe.path])

    return r

def attach_gdb():
    if args.GDB:
        gdb.attach(r, gdbscript="""
source ~/.gdbinit
b*main+ ...
        """)


def main():
    global r
    r = conn()
    attach_gdb()

    exe.symbols["main"] = 0xdeadbeef

if __name__ == "__main__":
    main()
