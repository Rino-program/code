// 文字列の配列を読み込んで表示

#include <stdio.h>

int main(void)
{
	char s[3][128];

	for (int i = 0; i < 3; i++) {
		printf("s[%d] : ", i);
		scanf("%s", s[i]);
	}

	for (int i = 0; i < 3; i++)
		printf("s[%d] = \"%s\"\n", i, s[i]);

	return 0;
}
