// gcc -g echo.c -o echo
#include <stdio.h>

int main(int argc, char *argv[])
{
	char data[32];

	scanf("%32s", data);
	printf("%s\n", data);

	return 0;
}
