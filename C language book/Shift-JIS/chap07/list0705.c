// 配列の要素数を求める

#include <stdio.h>

int main(void)
{
	int    a[5];
	double x[7];

	printf("配列aの要素数＝%zu\n", sizeof(a) / sizeof(a[0]));
	printf("配列xの要素数＝%zu\n", sizeof(x) / sizeof(x[0]));

	return 0;
}
