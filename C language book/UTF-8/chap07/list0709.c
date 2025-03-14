﻿// 0～65535を10進／2進／8進／16進で表示

#include <stdio.h>

//--- 整数x中のセットされたビット数を返す ---//
int count_bits(unsigned x)
{
	int bits = 0;
	while (x) {
		if (x & 1U) bits++;
		x >>= 1;
	}
	return bits;
}

//--- unsigned型のビット数を返す ---//
int int_bits(void)
{
	return count_bits(~0U);
}

//--- unsigned型整数xの下位nビットを表示 ---//
void print_nbits(unsigned x, unsigned n)
{
	int i = int_bits();
	i = (n < i) ? n - 1 : i - 1;
	for ( ; i >= 0; i--)
		putchar(((x >> i) & 1U) ? '1' : '0');
}

int main(void)
{
	for (unsigned i = 0; i <= 65535U; i++) {
		printf("%5u ", i);
		print_nbits(i, 16);
		printf(" %06o %04X\n", i, i);
	}

	return 0;
}
