// 左下が直角の直角二等辺三角形を表示

#include <stdio.h>

int main(void)
{
	int len;

	puts("左下直角二等辺三角形を表示します。");
	printf("短辺：");
	scanf("%d", &len);

	for (int i = 1; i <= len; i++) {	// i行（i = 1, 2, … , len）
		for (int j = 1; j <= i; j++)	// 各行にi個の'*'を表示
			putchar('*');
		putchar('\n');					// 改行
	}

	return 0;
}
