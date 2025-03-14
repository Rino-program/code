// ポインタ（アドレス演算子&と間接演算子*）

#include <stdio.h>

int main(void)
{
	int n = 57;
	printf("n  = %d\n", n);
	printf("&n = %p\n", &n);

	int *p = &n;
	printf("p  = %p\n", p);
	printf("*p = %d\n", *p);

	return 0;
}
