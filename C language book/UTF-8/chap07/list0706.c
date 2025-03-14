// ビット単位の論理演算

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

//--- unsigned型のビット内容を表示 ---//
void print_bits(unsigned x)
{
	for (int i = int_bits() - 1; i >= 0; i--)
		putchar(((x >> i) & 1U) ? '1' : '0');
}

int main(void)
{
	unsigned a, b;

	printf("非負の整数を二つ入力せよ。\n");
	printf("a : ");   scanf("%u", &a);
	printf("b : ");   scanf("%u", &b);

	putchar('\n');
	printf("a     = ");  print_bits(a);      putchar('\n');
	printf("b     = ");  print_bits(b);      putchar('\n');
	printf("a & b = ");  print_bits(a & b);  putchar('\n');  // 論理積
	printf("a | b = ");  print_bits(a | b);  putchar('\n');  // 論理和
	printf("a ^ b = ");  print_bits(a ^ b);  putchar('\n');  // 排他的論理和
	printf("~a    = ");  print_bits(~a);     putchar('\n');  // aの１の補数
	printf("~b    = ");  print_bits(~b);     putchar('\n');  // bの１の補数

	return 0;
}
