#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    const char *filename;
    struct stat fs;
    int r;

    // Check for correct number of arguments
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    filename = argv[1];

    // Get the file's current status
    r = stat(filename, &fs);
    if (r == -1) {
        fprintf(stderr, "Error reading '%s'\n", filename);
        exit(EXIT_FAILURE);
    }

    // Change file permissions to add write permissions for group and others
    r = chmod(filename, fs.st_mode | S_IWGRP | S_IWOTH);
    if (r != 0) {
        fprintf(stderr, "Unable to reset permissions on '%s'\n", filename);
        exit(EXIT_FAILURE);
    }

    // Print success message
    printf("Permissions for '%s' updated successfully.\n", filename);
    return 0;
}