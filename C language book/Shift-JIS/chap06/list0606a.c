// �ׂ�������߂�idouble�^��������int�^��������^����j

#include <stdio.h>

//--- x��n���Ԃ� ---//
double power(double x, int n)
{
	double tmp = 1.0;

	while (n-- > 0)
		tmp *= x;	// tmp��x���|����
	return tmp;
}

int main(void)
{
	printf("5��3���%.2f�ł��B\n", power(5, 3));

	return 0;
}
