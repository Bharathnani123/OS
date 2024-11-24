#include <stdio.h>
#include <unistd.h>
int main() {
 printf("Sleeping for 3 seconds...\n");
 sleep(3); // Pause execution for 3 seconds
 printf("Woke up after 3 seconds!\n");
 return 0;
}