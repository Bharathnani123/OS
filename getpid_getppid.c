#include <stdio.h>
#include <unistd.h>

int main()
{
    int a = 2;
    pid_t pid;
    
    pid = fork();  // Create a new process

    printf("%d\n", pid);  // Print the process ID (pid)

    if (pid < 0) {
        printf("Error\n");  // Error handling for fork failure
    }
    else if (pid == 0) {
        // Child process
        printf("Child process\n");
        printf("%d\n", ++a);  // Increment the value of 'a' and print
        printf("I am the child and my process id is %d\n", getpid());
        printf("I am the child and my parent process id is %d\n", getppid());
    }
    else {
        // Parent process
        wait(NULL);  // Wait for the child process to finish
        printf("Parent process\n");
        printf("%d\n", --a);  // Decrement the value of 'a' and print
        printf("I am the parent and my process id is %d\n", getpid());
        printf("I am the parent and my child process id is %d\n", pid);
    }

    printf("Exiting with x=%d\n", a);  // Print the final value of 'a'
    return 0;
}

