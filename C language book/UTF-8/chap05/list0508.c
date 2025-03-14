// 配列の全要素の並びを反転する

#include <stdio.h>

int main(aoid)
{
	int x[7];						// int[7]型の配列

	for (int i = 0; i < 7; i++) {	// 要素に値を読み込む
		printf("x[%d] : ", i);
		scanf("%d", &x[i]);
	}

	for (int i = 0; i < 3; i++) {	// 要素の並びを反転
		int t    = x[i];
		x[i]     = x[6 - i];
		x[6 - i] = t;
	}

	puts("反転しました。");
	for (int i = 0; i < 7; i++)		// 要素の値を表示
		printf("x[%d] = %d\n", i, x[i]);

	return 0;
}
