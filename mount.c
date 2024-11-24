#include <stdio.h>
#include <stdlib.h>
#include <sys/mount.h>

int main() {
    const char *source = "/dev/sda";        // The storage device you want to connect
    const char *target = "/mnt/hii";        // Where you want to attach it in your file system
    const char *filesystemtype = "ext4";   // The type of the storage device
    unsigned long mountflags = 0;          // Flags, e.g., MS_RDONLY for read-only
    const void *data = NULL;               // Optional data specific to the filesystem

    // Attempt to mount the device
    if (mount(source, target, filesystemtype, mountflags, data) == -1) {
        perror("Error mounting the storage device");
        return 1;
    }

    printf("Storage device mounted successfully at /mnt/hii.\n");
    return 0;
}