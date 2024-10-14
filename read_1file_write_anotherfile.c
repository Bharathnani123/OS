#include <sys/types.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>

int main() 
{
    int source_fd, target_fd, n;
    char buffer[1024]; // Buffer to store file content

    // Open the source file in read-only mode
    source_fd = open("source.txt", O_RDONLY);
    if (source_fd < 0) {
        perror("Error opening source file");
        exit(EXIT_FAILURE);
    }

    // Open the target file for writing (create if not exists, truncate if exists)
    target_fd = open("target.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (target_fd < 0) {
        perror("Error opening target file");
        close(source_fd);
        exit(EXIT_FAILURE);
    }

    // Read from the source file and write to the target file
    while ((n = read(source_fd, buffer, sizeof(buffer))) > 0) {
        if (write(target_fd, buffer, n) != n) {
            perror("Error writing to target file");
            close(source_fd);
            close(target_fd);
            exit(EXIT_FAILURE);
        }
    }

    // Check if there was an error reading the source file
    if (n < 0) {
        perror("Error reading source file");
    }

    // Close the files
    close(source_fd);
    close(target_fd);

    printf("File copied successfully.\n");

    return 0;
}
