// strncpy関数の利用例

#include <stdio.h>
#include <string.h>

int main(void)
{
	char s1[10];
	char *x = "XXXXXXXXX";	// 9個の'X'とナル文字

	strcpy(s1, x);  strncpy(s1, "12345", 3);  printf("s1 = %s\n", s1);

	strcpy(s1, x);  strncpy(s1, "12345", 5);  printf("s1 = %s\n", s1);

	strcpy(s1, x);  strncpy(s1, "12345", 7);  printf("s1 = %s\n", s1);

	return 0;
}
