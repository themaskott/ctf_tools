#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char * argv[]){
        setreuid(geteuid(), geteuid());
        execve("/bin/sh", 0, 0);

}
