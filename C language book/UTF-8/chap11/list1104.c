// 文字列の配列

#include <stdio.h>

int main(void)
{
	char a[][5] = {"LISP", "C", "Ada"};	  // 配列による文字列の配列
	char *p[]   = {"PAUL", "X", "MAC"};	  // ポインタによる文字列の配列

	for (int i = 0; i < 3; i++)
		printf("a[%d] = \"%s\"\n", i, a[i]);

	for (int i = 0; i < 3; i++)
		printf("p[%d] = \"%s\"\n", i, p[i]);

	return 0;
}
