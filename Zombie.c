#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    pid_t pid = fork();

    if (pid > 0) {
        // Parent process
        printf("Parent process is running (PID: %d).\n", getpid());
        printf("Child process (PID: %d) will become a zombie for 5 seconds.\n", pid);
        sleep(5); // Delay to allow the child to remain in a zombie state
        printf("Parent now calling wait() to clean up the child process.\n");
        wait(NULL); // Reap the zombie process
        printf("Child process cleaned up. No more zombie.\n");
    } else if (pid == 0) {
        // Child process
        printf("Child process (PID: %d) is exiting.\n", getpid());
        exit(0); // Child exits immediately
    } else {
        // Fork failed
        perror("Fork failed");
        exit(1);
    }

    return 0;
}
