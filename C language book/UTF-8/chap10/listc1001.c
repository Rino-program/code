﻿// 添字演算子と間接演算子

#include <stdio.h>

int main(void)
{
	int a[4];

	0[a] = a[1] = *(a + 2) = *(3 + a) = 7;

	for (int i = 0; i < 4; i++)
		printf("a[%d] = %d\n", i, a[i]);

	return 0;
}
