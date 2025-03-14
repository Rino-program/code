// 文字列"12345"を書式化して表示

#include <stdio.h>

int main(void)
{
	char str[] = "12345";

	printf("%s\n",   str);		// そのまま
	printf("%3s\n",  str);		// 最低３桁
	printf("%.3s\n", str);		// ３桁まで
	printf("%8s\n",  str);		// 最低８桁で右よせ
	printf("%-8s\n", str);		// 最低８桁で左よせ

	return 0;
}
