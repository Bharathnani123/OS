#include <sys/types.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>

int main() 
{
    int source_fd, target_fd, n;
    char buffer[11]; // To store characters from 10th to 20th plus the null terminator

    // Open the source file in read-only mode
    source_fd = open("source.txt", O_RDONLY);
    if (source_fd < 0) {
        perror("Error opening source file");
        exit(EXIT_FAILURE);
    }

    // Move the file pointer to the 10th character (position is 0-based, so seek to 9)
    off_t offset = lseek(source_fd, 9, SEEK_SET);
    if (offset == (off_t) -1) {
        perror("Error seeking in source file");
        close(source_fd);
        exit(EXIT_FAILURE);
    }

    // Read characters from 10th to 20th
    n = read(source_fd, buffer, 10);
    if (n < 0) {
        perror("Error reading source file");
        close(source_fd);
        exit(EXIT_FAILURE);
    }

    // Null-terminate the string
    buffer[10] = '\0';

    // Open the target file for writing (create if not exists, truncate if exists)
    target_fd = open("target.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (target_fd < 0) {
        perror("Error opening target file");
        close(source_fd);
        exit(EXIT_FAILURE);
    }

    // Write the characters to the target file
    if (write(target_fd, buffer, n) != n) {
        perror("Error writing to target file");
        close(source_fd);
        close(target_fd);
        exit(EXIT_FAILURE);
    }

    // Print the characters to the terminal
    printf("Characters from position 10 to 20: %s\n", buffer);

    // Close the files
    close(source_fd);
    close(target_fd);

    return 0;
}
