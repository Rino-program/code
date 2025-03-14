// 読み込んだ整数の個数だけ＊を連続表示（for文）

#include <stdio.h>

int main(void)
{
	int no;

	printf("正の整数：");
	scanf("%d", &no);

	for (int i = 1; i <= no; i++)
		putchar('*');
	putchar('\n');

	return 0;
}
