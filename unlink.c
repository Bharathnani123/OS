#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
    const char *fileName = "file_to_delete.txt";

    // Create the file
    FILE *file = fopen(fileName, "w");
    if (file == NULL) {
        perror("Error creating file");
        exit(EXIT_FAILURE);
    }

    // Write content to the file
    fprintf(file, "This file will be deleted.\n");
    fclose(file);

    // Use the unlink system call to delete the file
    if (unlink(fileName) == -1) {
        perror("Error deleting file");
        exit(EXIT_FAILURE);
    }

    printf("File deleted successfully.\n");
    return 0;
}