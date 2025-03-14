// 文字列をコピーする（別解）

#include <stdio.h>

//--- 文字列sをdにコピーする ---//
char *str_copy(char *d, const char *s)
{
	char *t = d;
	int i = 0;

	while (d[i] = s[i])
		i++;

	return t;
}

int main(void)
{
	char str[128] = "ABC";
	char tmp[128];

	printf("str = \"%s\"\n", str);

	printf("コピーするのは：", tmp);
	scanf("%s", tmp);

	str_copy(str, tmp);

	printf("str = \"%s\"\n", str);

	return 0;
}
