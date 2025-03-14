// 読み込んだ正の整数値までカウントアップ

#include <stdio.h>

int main(void)
{
	int no;

	printf("正の整数を入力せよ：");
	scanf("%d", &no);

	int i = 0;
	while (i <= no)
		printf("%d ", i++);		// iの値を表示した後にインクリメント
	printf("\n");				// 改行

	return 0;
}
