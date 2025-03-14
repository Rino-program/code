// 読み込んだ整数値を３で割った剰余を表示（if文）

#include <stdio.h>

int main(void)
{
	int no;

	printf("整数値：");
	scanf("%d", &no);

	if (no % 3 == 0)
		puts("３で割り切れます。");
	else if (no % 3 == 1)
		puts("３で割った剰余は１です。");
	else
		puts("３で割った剰余は２です。");

	return 0;
}
