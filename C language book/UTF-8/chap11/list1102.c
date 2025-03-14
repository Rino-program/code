// 配列による文字列の書きかえ

#include <stdio.h>

int main(void)
{
	char s[] = "ABC";

	printf("s = \"%s\"\n", s);

	s = "DEF";		// エラー

	printf("s = \"%s\"\n", s);

	return 0;
}
