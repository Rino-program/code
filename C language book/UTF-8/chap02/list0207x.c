// 二つの実数値の和・差・積・商・剰余を表示（エラー）

#include <stdio.h>

int main(void)
{
	double x, y;		// 浮動小数点数

	puts("二つの実数を入力せよ。");
	printf("実数x：");   scanf("%lf", &x);
	printf("実数y：");   scanf("%lf", &y);

	printf("x + y = %d\n", x + y);		// 和
	printf("x - y = %d\n", x - y);		// 差
	printf("x * y = %d\n", x * y);		// 積
	printf("x / y = %d\n", x / y);		// 商
	printf("x %% y = %d\n", x % y);		// エラー

	return 0;
}
