#include <sys/types.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>

int main() 
{
    int fd, n;
    char b[6]; // To store the last 5 characters plus the null terminator

    // Open the file in read-only mode
    fd = open("source.txt", O_RDONLY);
    if (fd < 0) {
        perror("Error opening file");
        exit(EXIT_FAILURE);
    }

    // Move the file pointer to the end of the file minus 5 bytes
    off_t offset = lseek(fd, -5, SEEK_END);
    if (offset == (off_t) -1) {
        perror("Error seeking in file");
        close(fd);
        exit(EXIT_FAILURE);
    }

    // Read the last 5 characters from the file
    n = read(fd, b, 5);
    if (n < 0) {
        perror("Error reading file");
        close(fd);
        exit(EXIT_FAILURE);
    }

    // Null-terminate the string
    b[5] = '\0';

    // Print the last 5 characters
    printf("Last 5 characters: %s\n", b);

    // Close the file
    close(fd);
    return 0;
}
