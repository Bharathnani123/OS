#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
int main()
{
	pid_t child_pid = fork();
	if (child_pid>0)
	{
		sleep(10);
		printf("Hello\n");
	}
	else
		exit(0);
	return 0;
}
