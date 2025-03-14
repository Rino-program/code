// 読み込んだ整数値は奇数であるか偶数であるか

#include <stdio.h>

int main(void)
{
	int n;

	printf("整数を入力せよ：");
	scanf("%d", &n);

	if (n % 2)
		puts("その数は奇数です。");
	else
		puts("その数は偶数です。");

	return 0;
}
