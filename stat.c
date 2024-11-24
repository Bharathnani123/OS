#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <unistd.h>

int main() {
    const char *filename = "example.txt";
    struct stat fileStat;

    // Create the file
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        perror("Error creating file");
        exit(EXIT_FAILURE);
    }

    // Write content to the file
    fprintf(file, "This is the content of the file.\n");
    fclose(file);

    // Get file information
    if (stat(filename, &fileStat) == -1) {
        perror("Error getting file information");
        return -1;
    }

    // Display file information
    printf("File Size: %ld bytes\n", fileStat.st_size);
    printf("File Permissions: %o\n", fileStat.st_mode & 0777);
    printf("Last Access Time: %ld\n", fileStat.st_atime);

    return 0;
}