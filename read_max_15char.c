#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main() 
{
    char buffer[16]; // Buffer to store 15 characters plus the null terminator
    int n;

    // Prompt the user to enter up to 15 characters
    printf("Enter up to 15 characters: ");

    // Read up to 15 characters from the user
    n = read(STDIN_FILENO, buffer, 15);
    if (n < 0) {
        perror("Error reading input");
        exit(EXIT_FAILURE);
    }

    // Null-terminate the string
    buffer[n] = '\0';

    // Print the entered characters
    printf("You entered: %s\n", buffer);

    return 0;
}
