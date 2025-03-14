// 型や変数の大きさを表示

#include <stdio.h>

int main(void)
{
	int    a, b;
	double x, y;

	printf("sizeof(int)    = %zu\n", sizeof(int));
	printf("sizeof(double) = %zu\n", sizeof(double));

	printf("sizeof(a)      = %zu\n", sizeof(a));
	printf("sizeof(x)      = %zu\n", sizeof(x));

	printf("sizeof(a + b)  = %zu\n", sizeof(a + b));
	printf("sizeof(a + y)  = %zu\n", sizeof(a + y));
	printf("sizeof(x + y)  = %zu\n", sizeof(x + y));

	return 0;
}
