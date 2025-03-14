// 二つの変数を初期化して表示

#include <stdio.h>

int main(void)
{
	int x = 57;							// xはint型の変数（57で初期化）
	int y = x + 12;						// yはint型の変数（x + 12で初期化）

	printf("xの値は%dです。\n", x);		// xの値を表示
	printf("yの値は%dです。\n", y);		// yの値を表示

	return 0;
}
