#include <unistd.h>
#include <stdio.h>
int main() {
 void *current_brk = sbrk(0); // Get the current program break
 printf("Current break: %p\n", current_brk);
 // Increase program break by 1024 bytes
 if (sbrk(1024) == (void *)-1) {
 perror("sbrk failed");
 return 1;
 }
 printf("New break: %p\n", sbrk(0)); // Check the new program break
 return 0;
}