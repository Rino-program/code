// 長方形を描画

#include <stdio.h>

int main(void)
{
	int height, width;

	puts("長方形を表示します。");
	printf("高さ：");   scanf("%d", &height);
	printf("横幅：");   scanf("%d", &width);

	for (int i = 1; i <= height; i++) {		// 長方形はheight行
		for (int j = 1; j <= width; j++)	// 各行にwidth個の'*'を表示
			putchar('*');
		putchar('\n');						// 改行
	}

	return 0;
}
