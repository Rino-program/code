// 読み込んだ整数の個数だけ＊を連続表示（for文：iの開始は1）

#include <stdio.h>

int main(void)
{
	int no;

	printf("正の整数：");
	scanf("%d", &no);

	for (int i = 0; i < no; i++)
		putchar('*');
	putchar('\n');

	return 0;
}
