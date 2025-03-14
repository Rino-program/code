﻿// 配列の一部の要素をゼロにする

#include <stdio.h>

//--- 要素数nの配列vの要素に0を代入 ---//
void set_zero(int v[], int n)
{
	for (int i = 0; i < n; i++)
		v[i] = 0;
}

//--- 要素数nの配列vの全要素を表示して改行 ---//
void print_array(const int v[], int n)
{
	printf("{ ");
	for (int i = 0; i < n; i++)
		printf("%d ", v[i]);
	printf("}\n");
}

int main(void)
{
	int ary1[] = {1, 2, 3, 4, 5};
	int ary2[] = {3, 2, 1};

	printf("ary1 = ");   print_array(ary1, 5);
	printf("ary2 = ");   print_array(ary2, 3);

	set_zero(ary1, 3);		// 配列ary1の先頭3要素に0を代入
	set_zero(ary2, 2);		// 配列ary2の先頭2要素に0を代入

	printf("両配列の一部の要素に0を代入しました。\n");
	printf("ary1 = ");   print_array(ary1, 5);
	printf("ary2 = ");   print_array(ary2, 3);

	return 0;
}
