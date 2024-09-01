#include <stdio.h>
#include <math.h>

void prepare()
{
	setvbuf(stdin, 0LL, 2, 0LL);
	setvbuf(stdout, 0LL, 2, 0LL);
	alarm(60);
}

int pow(int a, int b)
{
	int c = a;
	if (b == 0)
		return 1;

	for (; b > 1; b--)
	{
		c = a * c;
	}
	return c;
}

int main()
{
	int a, b, i, j;

	prepare();

	printf("Input your decimal number: ");
	scanf("%d", &a);

	printf("What do you want to turn it into: ");
	scanf("%d", &b);

	for (i = 0; i < 100; i++) {
		if (a <= pow(b, i))
			break;
	}

	printf("Result: ");
	for (; i > 0; i--) {
		j = a / pow(b, i - 1);
		printf("%d", j);
		a = a % (int)pow(b, i - 1);
	}
	putchar('\n');

	return 0;
}
