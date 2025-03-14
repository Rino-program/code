// 配列の要素のうち正の要素を別の配列にコピー

#include <stdio.h>

int main(void)
{
	int a[5];		// コピー元配列
	int b[5];		// コピー先配列

	for (int i = 0; i < 5; i++) {	// 要素に値を読み込む
		printf("a[%d] : ", i);
		scanf("%d", &a[i]);
	}

	int count = 0;					// コピーした要素数
	for (int i = 0; i < 5; i++)
		if (a[i] > 0)				// 正であれば
			b[count++] = a[i];		// コピー

	for (int i = 0; i < count; i++)
		printf("b[%d] = %d\n", i, b[i]);

	return 0;
}
