// 二つの整数を昇順に並べる

#include <stdio.h>

//--- xとyが指すオブジェクトの値を交換 ---//
void swap(int *x, int *y)
{
	int temp = *x;
	*x = *y;
	*y = temp;
}

//--- *n1≦*n2となるようにソート ---//
void sort2(int *n1, int *n2)
{
	if (*n1 > *n2)
		swap(n1, n2);
}

int main(void)
{
	int a, b;

	puts("二つの整数を入力せよ。");
	printf("整数Ａ：");   scanf("%d", &a);
	printf("整数Ｂ：");   scanf("%d", &b);

	sort2(&a, &b);

	puts("昇順にソートしました。");
	printf("整数Ａは%dです。\n", a);
	printf("整数Ｂは%dです。\n", b);

	return 0;
}
