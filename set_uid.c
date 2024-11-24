#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>
int main() {
 uid_t current_uid = getuid(); // Get current user ID
 printf("Current UID: %d\n", current_uid);
 if (setuid(1000) == 0) { // Change UID to 1000 (example)
 printf("Successfully changed UID to: %d\n", getuid());
 } else {
 perror("setuid failed");
 exit(1);
 }
 return 0;
}