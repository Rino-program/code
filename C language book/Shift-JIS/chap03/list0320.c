// 読み込んだ整数値を３で割った剰余を表示（switch文）

#include <stdio.h>

int main(void)
{
	int no;

	printf("整数値：");
	scanf("%d", &no);

	switch (no % 3) {									// no % 3が
	 case 0 : puts("３で割り切れます。");		break;	// 0であれば…
	 case 1 : puts("３で割った剰余は１です。"); break;	// 1であれば…
	 case 2 : puts("３で割った剰余は２です。"); break;	// 2であれば…
	}

	return 0;
}
