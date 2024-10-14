#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>   // For exit()
#include <string.h>   // For strlen()
#include <unistd.h>   // For close() and write()

int main()
{
    int sz;

    int fd = open("foo.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd < 0)
    {
        perror("Error opening file");
        exit(1);
    }

    sz = write(fd, "hello geeks\n", strlen("hello geeks\n"));

    if (sz < 0)
    {
        perror("Error writing to file");
        close(fd);
        exit(1);
    }

    printf("Called write(%d, \"hello geeks\\n\", %zu). It returned %d\n", fd, strlen("hello geeks\n"), sz);

    close(fd);
    return 0;
}
