#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>

int main(void) {
    printf("maintenance agent demo\n");
    system("echo demo"); /* noqa: demo signal for VESTA */
    return 0;
}

