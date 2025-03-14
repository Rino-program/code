// 二つの整数値を交換する

#include <stdio.h>

//--- ２値の交換（xとyが指すオブジェクトの値の交換）---//
void swap(int *x, int *y)
{
	int temp = *x;
	*x = *y;
	*y = temp;
}

int main(void)
{
	int a, b;

	puts("二つの整数を入力せよ。");
	printf("整数Ａ：");   scanf("%d", &a);
	printf("整数Ｂ：");   scanf("%d", &b);

	swap(&a, &b);

	puts("これらの値を交換しました。");
	printf("整数Ａは%dです。\n", a);
	printf("整数Ｂは%dです。\n", b);

	return 0;
}
