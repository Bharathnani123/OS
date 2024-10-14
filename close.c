// C program to illustrate close system call
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>  // Include this header to properly declare exit

int main()
{
    int fd1 = open("foo.txt", O_RDONLY);
    if (fd1 < 0) {
        perror("c1");
        exit(1);  // Properly declared exit function
    }
    printf("opened the fd = %d\n", fd1);

    // Using close system call
    if (close(fd1) < 0) {
        perror("c1");
        exit(1);  // Properly declared exit function
    }
    printf("closed the fd.\n");

    return 0;
}
