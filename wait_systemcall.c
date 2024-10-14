#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h> // Include this header for the wait() function

int main() {
    pid_t pid; // Variable to store process ID
    pid = fork(); // Create a new process

    if (pid < 0) {
        // Fork failed
        printf("Fork failed\n");
        return 1; // Exit with error
    }
    else if (pid == 0) {
        // Child process
        printf("Child process (PID: %d) is executing...\n", getpid());
        sleep(3); // Simulate some work by sleeping for 3 seconds
        printf("Child process (PID: %d) is done.\n", getpid());
        exit(0); // Exit the child process
    }
    else {
        // Parent process
        printf("Parent process (PID: %d) is waiting for the child to complete...\n", getpid());
        wait(NULL); // Wait for the child process to finish
        printf("Child process has completed. Parent process is continuing...\n");
    }

    return 0; // Exit successfully
}
