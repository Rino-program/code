// 配列の全要素を別の配列にコピー（誤り）

#include <stdio.h>

int main(void)
{
	int a[5];		// コピー元配列
	int b[5];		// コピー先配列

	for (int i = 0; i < 5; i++) {	// 要素に値を読み込む
		printf("a[%d] : ", i);
		scanf("%d", &a[i]);
	}

	b = a;			// エラー：配列の代入はできない

	puts("  a    b");
	puts("---------");
	for (int i = 0; i < 5; i++)
		printf("%4d%4d\n", a[i], b[i]);

	return 0;
}
