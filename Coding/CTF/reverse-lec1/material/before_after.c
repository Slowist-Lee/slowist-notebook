// gcc -g before_after.c -o before_after
#include <stdio.h>
#include <stdlib.h>

__attribute__((constructor)) void func1()
{
	printf("Before main()\n");
}

__attribute__((constructor)) void func2()
{
	printf("After main()\n");
}

int main(int argc, char *argv[])
{
	printf("During main()\n");
}
