// 文字列をコピーして表示

#include <stdio.h>
#include <string.h>

int main(void)
{
	char st[128];
	char s1[128], s2[128];

	printf("文字列：", st);
	scanf("%s", st);

	printf("s2 = \"%s\"\n", strcpy(s2, st));	// stをs2にコピーして表示
	printf("s1 = \"%s\"\n", strcpy(s1, s2));	// s2をs1にコピーして表示

	return 0;
}
