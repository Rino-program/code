// 二つの変数に整数値を代入して表示

#include <stdio.h>

int main(void)
{
	int x, y;							// xとyはint型の変数

	x = 57;								// xに57を代入
	y = x + 12;							// yにx + 12を代入

	printf("xの値は%dです。\n", x);		// xの値を表示
	printf("yの値は%dです。\n", y);		// yの値を表示

	return 0;
}
