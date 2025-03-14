// 階乗を再帰的に求める（条件演算子）

#include <stdio.h>

//--- 整数値nの階乗値を返却（条件演算子） ---//
int factorial(int n)
{
	return n > 0 ? n * factorial(n - 1) : 1;
}

int main(void)
{
	int num;

	printf("整数を入力せよ：");
	scanf("%d", &num);

	printf("%dの階乗は%dです。\n", num, factorial(num));

	return 0;
}
