﻿// 読み込んだ二つの整数値の大きいほうの値を表示（その２）
// 別解（if文が制御する文を複合文にする）


#include <stdio.h>

int main(void)
{
	int n1, n2;

	puts("二つの整数を入力せよ。");
	printf("整数１：");   scanf("%d", &n1);
	printf("整数２：");   scanf("%d", &n2);

	int max;
	if (n1 > n2) {
		max = n1;
	} else {
		max = n2;
	}
	printf("大きいほうの値は%dです。\n", max);

	return 0;
}
