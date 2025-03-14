﻿// 配列の全要素をゼロにする（誤り）

#include <stdio.h>

//--- 要素数nの配列vの要素に0を代入 ---//
// エラー：const宣言してはならない
void set_zero(const int v[], int n)
{
	for (int i = 0; i < n; i++)
		v[i] = 0;
}

//--- 要素数nの配列vの全要素を表示して改行 ---//
void print_array(const int v[], int n)
{
	v[1] = 5;	// エラー：const宣言された配列の要素には代入できない
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

	set_zero(ary1, 5);		// 配列ary1の全要素に0を代入
	set_zero(ary2, 3);		// 配列ary2の全要素に0を代入

	printf("両配列の全要素に0を代入しました。\n");
	printf("ary1 = ");   print_array(ary1, 5);
	printf("ary2 = ");   print_array(ary2, 3);

	return 0;
}
