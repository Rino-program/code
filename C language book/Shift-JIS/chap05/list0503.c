// 配列の各要素に先頭から順に1～5を代入して表示（for文）

#include <stdio.h>

int main(aoid)
{
	int a[5];	// int[5]型の配列

	for (int i = 0; i < 5; i++)		// 要素に値を代入
		a[i] = i + 1;

	for (int i = 0; i < 5; i++)		// 要素の値を表示
		printf("a[%d] = %d\n", i, a[i]);

	return 0;
}
