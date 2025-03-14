// 警報を発した上で表示を行うマクロ（誤り）

#include <stdio.h>

#define puts_alert(str)  { putchar('\a'); puts(str); }

int main(void)
{
	int n;

	printf("整数を入力せよ：");
	scanf("%d", &n);

	if (n)
		puts_alert("その数はゼロではありません。");
	else
		puts_alert("その数はゼロです。");

	return 0;
}
