// 読み込んだ整数値は奇数か

#include <stdio.h>

int main(void)
{
	int n;

	printf("整数を入力せよ：");
	scanf("%d", &n);

	if (n % 2)
		puts("その数は奇数です。");

	return 0;
}
