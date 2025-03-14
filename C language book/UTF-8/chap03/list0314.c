// 読み込んだ二つの整数値の大きいほうの値を表示（その３：条件演算子）

#include <stdio.h>

int main(void)
{
	int n1, n2;

	puts("二つの整数を入力せよ。");
	printf("整数１：");   scanf("%d", &n1);
	printf("整数２：");   scanf("%d", &n2);

	int max = n1 > n2 ? n1 : n2;		// 大きいほうの値でmaxを初期化

	printf("大きいほうの値は%dです。\n", max);

	return 0;
}
