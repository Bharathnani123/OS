#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <errno.h>

int main(int argc, char *argv[]) {
    int pid, status;
    
    pid = fork();  // Create a new process
    
    if (pid < 0) {
        // Handle fork failure
        perror("Fork failed");
    }
    else if (pid == 0) {
        // Child process
        execl("/bin/ls", "ls", NULL);  // Execute the ls command
        // If execl fails, we print an error and exit
        perror("execl failed");
        exit(1);
    }
    else {
        // Parent process
        wait(&status);  // Wait for child process to finish
        if (WIFEXITED(status)) {
            printf("Child process completed with exit status %d\n", WEXITSTATUS(status));
        } else {
            printf("Child process terminated abnormally\n");
        }
    }
    
    return 0;
}
