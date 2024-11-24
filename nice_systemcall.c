#include <stdio.h>
#include <unistd.h>
#include <sys/resource.h> // Required for getpriority(), setpriority(), and PRIO_PROCESS
#include <errno.h> // For errno handling
int main() {
 // Get the current priority of the process
 int priority = getpriority(PRIO_PROCESS, 0);
 if (priority == -1 && errno != 0) {
 perror("getpriority failed");
 } else {
 printf("Current priority: %d\n", priority);
 }
 // Change process priority using nice()
 int new_priority = nice(5); // Add 5 to the current niceness
 if (new_priority == -1 && errno != 0) {
 perror("nice failed");
 } else {
 printf("New priority after nice(5): %d\n", getpriority(PRIO_PROCESS, 0));
 }
 return 0;
}