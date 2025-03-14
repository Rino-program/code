// 階乗を再帰的に求める

#include <stdio.h>

//--- 整数値nの階乗値を返却 ---//
int factorial(int n)
{
	if (n > 0)
		return n * factorial(n - 1);
	else
		return 1;
}

int main(void)
{
	int num;

	printf("整数を入力せよ：");
	scanf("%d", &num);

	printf("%dの階乗は%dです。\n", num, factorial(num));

	return 0;
}
