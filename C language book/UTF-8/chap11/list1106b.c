// 文字列をコピーする（str_copyの返却値を有効活用）

#include <stdio.h>

//--- 文字列sをdにコピーする ---//
char *str_copy(char *d, const char *s)
{
	char *t = d;

	while (*d++ = *s++)
		;
	return t;
}

int main(void)
{
	char str[128] = "ABC";
	char tmp[128];

	printf("str = \"%s\"\n", str);

	printf("コピーするのは：", tmp);
	scanf("%s", tmp);

	printf("str = \"%s\"\n", str_copy(str, tmp));	// コピーした上で表示

	return 0;
}
