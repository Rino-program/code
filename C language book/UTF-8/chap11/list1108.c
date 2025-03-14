// strlen関数の利用例

#include <stdio.h>
#include <string.h>

int main(void)
{
	char str[128];

	printf("文字列：");
	scanf("%s", str);

	printf("文字列\"%s\"の長さは%zuです。\n", str, strlen(str));

	return 0;
}
