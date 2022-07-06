#!/bin/bash

# Quickly run a set of commands to summarize useful informations about a binary/library

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <binary>"
    exit 0
fi

BIN="$1"

echo "[+] Analysing : $BIN"
echo

echo "[>] file :"
file "$BIN"
echo

echo "[>] ldd :"
ldd -v "$BIN"
echo

echo "[>] objdump :"
objdump -f "$BIN"
echo

objdump -x "$BIN" | grep -A 4 "Références de version:"
echo

objdump -S "$BIN" | grep puts | grep -A 1 ">:"
echo

objdump -S "$BIN" | grep system | grep -A 1 ">:"
echo

echo "[>] strings :"
strings -t x "$BIN" | grep "/bin/sh"
echo

echo "[>] checksec :"
checksec --file="$BIN"
echo

echo "[>] gadgets :"
ROPgadget --binary "$BIN" | grep ": pop rdi ; ret"
