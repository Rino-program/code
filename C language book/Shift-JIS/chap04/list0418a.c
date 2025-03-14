// 九九の表を表示（表示するのには40以下のみ）

#include <stdio.h>

int main(void)
{
	for (int i = 1; i <= 9; i++) {
		for (int j = 1; j <= 9; j++) {
			int seki = i * j;
			if (seki > 40)
				break;
			printf("%3d", seki);
		}
		putchar('\n');		// 改行
	}

	return 0;
}
