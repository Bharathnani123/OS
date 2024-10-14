// C program to illustrate
// read system call
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>  // Include this header for calloc and exit

int main()
{
    int fd, sz;
    char* c = (char*)calloc(100, sizeof(char));  // Properly declared calloc

    fd = open("foo.txt", O_RDONLY);
    if (fd < 0) {
        perror("r1");
        exit(1);  // Properly declared exit function
    }

    sz = read(fd, c, 10);
    printf("called read(%d, c, 10). returned that %d bytes were read.\n", fd, sz);
    c[sz] = '\0';
    printf("Those bytes are as follows: %s\n", c);  // Removed extra space in %s

    free(c);  // Free the allocated memory
    return 0;
}
