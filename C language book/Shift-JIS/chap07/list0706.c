// �r�b�g�P�ʂ̘_�����Z

#include <stdio.h>

//--- ����x���̃Z�b�g���ꂽ�r�b�g����Ԃ� ---//
int count_bits(unsigned x)
{
	int bits = 0;
	while (x) {
		if (x & 1U) bits++;
		x >>= 1;
	}
	return bits;
}

//--- unsigned�^�̃r�b�g����Ԃ� ---//
int int_bits(void)
{
	return count_bits(~0U);
}

//--- unsigned�^�̃r�b�g���e��\�� ---//
void print_bits(unsigned x)
{
	for (int i = int_bits() - 1; i >= 0; i--)
		putchar(((x >> i) & 1U) ? '1' : '0');
}

int main(void)
{
	unsigned a, b;

	printf("�񕉂̐��������͂���B\n");
	printf("a : ");   scanf("%u", &a);
	printf("b : ");   scanf("%u", &b);

	putchar('\n');
	printf("a     = ");  print_bits(a);      putchar('\n');
	printf("b     = ");  print_bits(b);      putchar('\n');
	printf("a & b = ");  print_bits(a & b);  putchar('\n');  // �_����
	printf("a | b = ");  print_bits(a | b);  putchar('\n');  // �_���a
	printf("a ^ b = ");  print_bits(a ^ b);  putchar('\n');  // �r���I�_���a
	printf("~a    = ");  print_bits(~a);     putchar('\n');  // a�̂P�̕␔
	printf("~b    = ");  print_bits(~b);     putchar('\n');  // b�̂P�̕␔

	return 0;
}
