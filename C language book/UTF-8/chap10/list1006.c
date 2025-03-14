// 二つの整数の和と差を求める

#include <stdio.h>

//--- n1とn2の和と差を*sumと*diffに格納 ---//
void sum_diff(int n1, int n2, int *sum, int *diff)
{ 
	*sum  = n1 + n2;
	*diff = n1 > n2 ? n1 - n2 : n2 - n1;
}

int main(void)
{
	int a, b;
	int wa = 0, sa = 0;

	puts("二つの整数を入力せよ。");
	printf("整数Ａ：");   scanf("%d", &a);
	printf("整数Ｂ：");   scanf("%d", &b);

	sum_diff(a, b, &wa, &sa);

	printf("和は%dで差は%dです。\n", wa, sa);

	return 0;
}
