#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
    const char *existingFileName = "existing_file.txt";
    const char *newLinkName = "hard_link.txt";

    // Create a file (if it doesn't exist)
    FILE *file = fopen(existingFileName, "w");
    if (file == NULL) {
        perror("Error creating file");
        exit(EXIT_FAILURE);
    }

    // Write content to the file
    fprintf(file, "This is the content of the file.\n");
    fclose(file);

    // Use the link system call to create a hard link
    if (link(existingFileName, newLinkName) == -1) {
        perror("Error creating hard link");
        exit(EXIT_FAILURE);
    }

    printf("Hard link created successfully.\n");
    return 0;
}
