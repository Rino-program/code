// ポインタの指す先を実行時に決定（別解）

#include <stdio.h>

int main(void)
{
	int x = 123;
	int y = 456;
	int sw;

	printf("x = %d\n", x);
	printf("y = %d\n", y);

	printf("変更するのは [0…x / 1…y] = ");
	scanf("%d", &sw);

	int *p = sw == 0 ? &x : &y;

	*p = 999;

	printf("x = %d\n", x);
	printf("y = %d\n", y);

	return 0;
}
