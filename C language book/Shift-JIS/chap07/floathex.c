// ���������_�^�̕ϐ��̒l��16�i���ŕ\��

#include <stdio.h>

int main(void)
{
	float a       = 123456789012345678901234567890.0;
	double b      = 123456789012345678901234567890.0;
	long double c = 123456789012345678901234567890.0;

	printf("a = %a\n",  a);
	printf("b = %a\n",  b);
	printf("c = %La\n", c);

	return 0;
}
