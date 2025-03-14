// 配列の要素の初期化

#include <stdio.h>

int main(void)
{
	int a[4] = {
		1868,		// 明治の最初の西暦年
		1912,		// 大正の最初の西暦年
		1926,		// 昭和の最初の西暦年
		1989,		// 平成の最初の西暦年
	};

	int b[] = {1, 2, 3};  // 要素数は3となる

	int c[5] = {1, 2};	  // int c[5] = {1, 2, 0, 0, 0}; と同じ 

	int d[5] = {0};		  // 全要素を0で初期化

	for (int i = 0; i < 4; i++)
		printf("a[%d] = %d\n", i, a[i]);
	putchar('\n');

	for (int i = 0; i < 3; i++)
		printf("b[%d] = %d\n", i, b[i]);
	putchar('\n');

	for (int i = 0; i < 5; i++)
		printf("c[%d] = %d\n", i, c[i]);
	putchar('\n');

	for (int i = 0; i < 5; i++)
		printf("d[%d] = %d\n", i, d[i]);
	putchar('\n');

	return 0;
}
