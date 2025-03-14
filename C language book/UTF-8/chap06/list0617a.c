// 識別子の有効範囲を確認する（不正）

#include <stdio.h>

int x = 75;						// Ａファイル有効範囲

void print_x(void)
{
	printf("x = %d\n", x);
}

int main(void)
{
	int i;
	// xを自身の不定値で初期化
	int x = x;					// Ｂブロック有効範囲

	print_x();

	printf("x = %d\n", x);

	for (i = 0; i < 5; i++) {
		int x = i * 100;		// Ｃブロック有効範囲
		printf("x = %d\n", x);
	}

	printf("x = %d\n", x);

	return 0;
}
