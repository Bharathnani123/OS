#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main()
{
    int fd;
    off_t offset;

    // Open a file for reading and writing
    fd = open("foo.txt", O_RDWR | O_CREAT, 0644);
    if (fd < 0)
    {
        perror("Error opening file");
        printf("Execution failed with error code 1\n");
        return 1; // Return 1 to indicate an error opening the file
    }

    // Write some initial data
    if (write(fd, "Hello, World!\n", 14) != 14)
    {
        perror("Error writing initial data");
        close(fd);
        printf("Execution failed with error code 2\n");
        return 2; // Return 2 to indicate an error writing initial data
    }

    // Move file pointer to the beginning
    offset = lseek(fd, 0, SEEK_SET);
    if (offset == (off_t) -1)
    {
        perror("Error seeking to start of file");
        close(fd);
        printf("Execution failed with error code 3\n");
        return 3; // Return 3 to indicate an error seeking to the start of the file
    }

    // Write data at the beginning of the file
    if (write(fd, "Start of File\n", 14) != 14)
    {
        perror("Error writing data at start of file");
        close(fd);
        printf("Execution failed with error code 4\n");
        return 4; // Return 4 to indicate an error writing data at the start of the file
    }

    // Move file pointer to the end of the file
    offset = lseek(fd, 0, SEEK_END);
    if (offset == (off_t) -1)
    {
        perror("Error seeking to end of file");
        close(fd);
        printf("Execution failed with error code 5\n");
        return 5; // Return 5 to indicate an error seeking to the end of the file
    }

    // Write data at the end of the file
    if (write(fd, "End of File\n", 12) != 12)
    {
        perror("Error writing data at end of file");
        close(fd);
        printf("Execution failed with error code 6\n");
        return 6; // Return 6 to indicate an error writing data at the end of the file
    }

    // Close the file
    if (close(fd) < 0)
    {
        perror("Error closing file");
        printf("Execution failed with error code 7\n");
        return 7; // Return 7 to indicate an error closing the file
    }

    // Print success message and return success code
    printf("Execution succeeded. Return code 0\n");
    return 0; // Return 0 to indicate successful execution
}
