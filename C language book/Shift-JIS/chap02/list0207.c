// 二つの実数値の和・差・積・商を実数で表示

#include <stdio.h>

int main(void)
{
	double x, y;		// 浮動小数点数

	puts("二つの実数を入力せよ。");
	printf("実数x：");   scanf("%lf", &x);
	printf("実数y：");   scanf("%lf", &y);

	printf("x + y = %f\n", x + y);		// 和
	printf("x - y = %f\n", x - y);		// 差
	printf("x * y = %f\n", x * y);		// 積
	printf("x / y = %f\n", x / y);		// 商

	return 0;
}
