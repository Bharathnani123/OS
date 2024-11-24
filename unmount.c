#include <sys/umount.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
    const char *target = "/mnt/mydrive";

    // Attempt to unmount the filesystem
    if (umount(target) == -1) {
        perror("Error unmounting filesystem");
        exit(EXIT_FAILURE);
    }

    printf("Filesystem unmounted successfully.\n");
    return 0;
}