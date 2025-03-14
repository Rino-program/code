// 整数型の大きさを表示する

#include <stdio.h>

int main(void)
{
	printf("sizeof(char)      = %zu\n", sizeof(char));
	printf("sizeof(short)     = %zu\n", sizeof(short));
	printf("sizeof(int)       = %zu\n", sizeof(int));
	printf("sizeof(long)      = %zu\n", sizeof(long));
	printf("sizeof(long long) = %zu\n", sizeof(long long));

	return 0;
}
