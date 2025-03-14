// 第３章 まとめ（３）大きいほうの値と差を表示

#include <stdio.h>

int main(void)
{
	int n1, n2;

	puts("二つの整数を入力せよ。");
	printf("整数１：");   scanf("%d", &n1);
	printf("整数２：");   scanf("%d", &n2);

	if (n1 > n2) {
		printf("大きいのはn1です。\n");
		printf("差は%dです。\n", n1 - n2);
	} else {
		printf("大きいのはn2です。\n");
		printf("差は%dです。\n", n2 - n1);
	}

	return 0;
}
