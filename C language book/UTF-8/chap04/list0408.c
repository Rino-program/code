// 読み込んだ整数の個数だけ＊を連続表示

#include <stdio.h>

int main(void)
{
	int no;

	printf("正の整数：");
	scanf("%d", &no);

	while (no-- > 0)
		putchar('*');
	putchar('\n');

	return 0;
}
