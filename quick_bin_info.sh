#!/bin/bash

# Quickly run a set of commands to summarize useful informations about a binary/library

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <binary>"
    exit 0
fi

BIN="$1"


banner(){
  echo "[>>> $1]"
}



echo "[+] Analysing : $BIN"
echo

banner "hashes :"
echo -n "MD5 : "
md5sum "$BIN"
echo -n "SHA1 : "
sha1sum "$BIN"
echo -n "SH256 : "
sha256sum "$BIN"
echo -n "SHA512 : "
sha512sum "$BIN"
echo

banner "ls :"
ls -la "$BIN"
echo

banner "file :"
file "$BIN"
echo

banner "ldd :"
ldd -v "$BIN"
echo

banner "objdump :"
objdump -f "$BIN"
echo

objdump -x "$BIN" | grep -A 4 "Références de version:"
echo

objdump -S "$BIN" | grep puts | grep -A 1 ">:"
echo

objdump -S "$BIN" | grep system | grep -A 1 ">:"
echo

banner "strings :"
strings -t x "$BIN" | grep "/bin/sh"
echo

banner "checksec :"
checksec --file="$BIN"
echo

banner "gadgets :"
ROPgadget --binary "$BIN" | grep ": pop rdi ; ret"
