// EOFの値と数字文字の値を表示（別解）

#include <stdio.h>

int main(void)
{
	printf("EOF ＝ %d\n", EOF);

	for (int i = 0; i < 10; i++)
		printf("'%d' ＝ %d\n", i, '0' + i);

	return 0;
}
