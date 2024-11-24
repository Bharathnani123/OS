PROGRAM:
#include <stdio.h> #include <stdlib.h> #include <sys/types.h> #include <unistd.h>
int main( int argc, char** argv )
{
int i;
int ecode = 0;
for( i = 1; i < argc; i++ )
{
if( chown( argv[i], 1000, 24 ) == 0 )
{
perror( argv[i] ); ecode++;
}
}
exit( ecode );
}
