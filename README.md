# ctf_tools

Just some empty scripts to save time during CTF


### Quick binary information

```bash
$ ./quick_bin_info.sh ../../test/chall
[+] Analysing : ../../test/chall

[>>> hashes :]
MD5 : 64ce8b3930a2d79d1e35291026b67202  ../../test/chall
SHA1 : cd0cac1365266c7bae31c6f5f846b5fbcc4cb5c0  ../../test/chall
SH256 : 71e797094c8d2780e7c35362c667c1c819fff0d2e579a9dda3a09642043d6e7f  ../../test/chall
SHA512 : 451ab2ed9e050a815e98653278d52003f2257d6d280cc5b9ec1e24fe9dfa6b6da6043b8609d1afc1c76f1dc6a0cc81f59aec9efaa5c0521052161f6232106b02  ../../test/chall

[>>> ls :]
-rwxr-xr-x 1 mk mk 16760  6 juil. 15:10 ../../test/chall

[>>> file :]
../../test/chall: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=62204d730127917f105d41a188515bf554be5bf8, for GNU/Linux 3.2.0, not stripped

[>>> ldd :]
	linux-vdso.so.1 (0x00007fff14f40000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f3d5f6de000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f3d5f8c1000)

	Version information:
	../../test/chall:
		libc.so.6 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libc.so.6
	/lib/x86_64-linux-gnu/libc.so.6:
		ld-linux-x86-64.so.2 (GLIBC_2.3) => /lib64/ld-linux-x86-64.so.2
		ld-linux-x86-64.so.2 (GLIBC_PRIVATE) => /lib64/ld-linux-x86-64.so.2

./quick_bin_info.sh: ligne 45: benner : commande introuvable

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

[>>> strings :]
   201a /bin/sh

[>>> checksec :]
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH	Symbols		FORTIFY	Fortified	Fortifiable	FILE
Partial RELRO   No canary found   NX enabled    PIE enabled     No RPATH   No RUNPATH   67) Symbols	  No	0		0		../../test/chall

[>>> gadgets :]
0x000000000000122b : pop rdi ; ret

```
