// 二つの実数値の和・差・積・商・剰余を表示（エラー）
// エラー文が出てしまって気になってしまうため、本文と一部変えてます
#include <stdio.h>

int main(void)
{
	//double x, y;  // 浮動小数点数
	int x, y;

	puts("二つの実数を入力せよ。");
	//printf("実数x：");   scanf("%lf", &x);
	//printf("実数y：");   scanf("%lf", &y);
	printf("実数x：");   scanf("%d", &x);
	printf("実数y：");   scanf("%d", &y);

	printf("x + y = %d\n", x + y);		// 和
	printf("x - y = %d\n", x - y);		// 差
	printf("x * y = %d\n", x * y);		// 積
	printf("x / y = %d\n", x / y);		// 商
	printf("x %% y = %d\n", x % y);		// エラー

	return 0;
}
