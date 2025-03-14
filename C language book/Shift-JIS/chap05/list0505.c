// 配列の各要素を先頭から順に1～5で初期化して表示

#include <stdio.h>

int main(aoid)
{
	int a[5] = {1, 2, 3, 4, 5};		// 初期化

	for (int i = 0; i < 5; i++)		// 要素の値を表示
		printf("a[%d] = %d\n", i, a[i]);

	return 0;
}
