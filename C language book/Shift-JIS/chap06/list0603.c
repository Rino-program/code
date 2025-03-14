// 二つの整数の２乗値の差を求める

#include <stdio.h>

//--- nの２乗値を返す ---//
int sqr(int n)
{
	return n * n;
}

//--- aとbの差を返す ---//
int diff(int a, int b)
{
	return a > b ? a - b : b - a;		// 大きいほうから小さいほうを引く
}

int main(void)
{
	int x, y;

	puts("二つの整数を入力せよ。");
	printf("整数x：");   scanf("%d", &x);
	printf("整数y：");   scanf("%d", &y);

	printf("xの2乗とyの2乗の差は%dです。\n", diff(sqr(x), sqr(y)));

	return 0;
}
