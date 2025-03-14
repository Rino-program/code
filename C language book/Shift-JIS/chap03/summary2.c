// 第３章 まとめ（２）整数値に応じて赤／青／白を表示

#include <stdio.h>

int main(void)
{
	int sw;

	printf("整数を入力せよ：");
	scanf("%d", &sw);

	switch (sw) {
	 case 1 : printf("赤");  break;
	 case 2 : printf("青");  break;
	 case 3 : printf("白");  break;
	}

	return 0;
}
