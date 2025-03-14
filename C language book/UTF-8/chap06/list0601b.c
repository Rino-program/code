// 二つの整数の大きいほうの値を求める（別解ｂ）

#include <stdio.h>

//--- 大きいほうの値を返す ---//
int max2(int a, int b)
{
	int max = a;

	if (b > max)
		max = b;

	return max;
}

int main(void)
{
	int n1, n2;

	puts("二つの整数を入力せよ。");
	printf("整数１：");   scanf("%d", &n1);
	printf("整数２：");   scanf("%d", &n2);

	printf("大きいほうの値は%dです。\n", max2(n1, n2));

	return 0;
}
