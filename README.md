# ctf_tools

Just some empty scripts to save time during CTF


### Quick binary information

```shell-session
$ ./quick_bin_info.sh ../../test/chall                                                                                                                                                                                           ✔  16:01:19 
[+] Analysing : ../../test/chall


[>] file :
../../test/chall: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=62204d730127917f105d41a188515bf554be5bf8, for GNU/Linux 3.2.0, not stripped

[>] ldd :
	linux-vdso.so.1 (0x00007ffe9c1db000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f2d05993000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f2d05b76000)

	Version information:
	../../test/chall:
		libc.so.6 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libc.so.6
	/lib/x86_64-linux-gnu/libc.so.6:
		ld-linux-x86-64.so.2 (GLIBC_2.3) => /lib64/ld-linux-x86-64.so.2
		ld-linux-x86-64.so.2 (GLIBC_PRIVATE) => /lib64/ld-linux-x86-64.so.2

[>] objdump :

../../test/chall:     format de fichier elf64-x86-64
architecture: i386:x86-64, fanions 0x00000150:
HAS_SYMS, DYNAMIC, D_PAGED
adresse de départ 0x0000000000001080


Références de version:
 requis par libc.so.6:
    0x09691a75 0x00 02 GLIBC_2.2.5

Sections :

0000000000001040 <puts@plt>:
    1040:	ff 25 da 2f 00 00    	jmpq   *0x2fda(%rip)        # 4020 <puts@GLIBC_2.2.5>

0000000000001050 <system@plt>:
    1050:	ff 25 d2 2f 00 00    	jmpq   *0x2fd2(%rip)        # 4028 <system@GLIBC_2.2.5>

[>] strings :
   201a /bin/sh

[>] checksec :
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH	Symbols		FORTIFY	Fortified	Fortifiable	FILE
Partial RELRO   No canary found   NX enabled    PIE enabled     No RPATH   No RUNPATH   67) Symbols	  No	0		0		../../test/chall

[>] gadgets :
0x000000000000122b : pop rdi ; ret
```
