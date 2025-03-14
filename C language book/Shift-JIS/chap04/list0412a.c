// 読み込んだ正の整数値までカウントアップしてカウントダウン

#include <stdio.h>

int main(void)
{
	int no;

	printf("正の整数を入力せよ：");
	scanf("%d", &no);

	for (int i = 0; i <= no; i++)
		printf("%d ", i);
	putchar('\n');		// 改行

	for (int i = no; i >= 0; i--)
		printf("%d ", i);
	putchar('\n');		// 改行

	return 0;
}
