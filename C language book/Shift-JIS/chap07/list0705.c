// �z��̗v�f�������߂�

#include <stdio.h>

int main(void)
{
	int    a[5];
	double x[7];

	printf("�z��a�̗v�f����%zu\n", sizeof(a) / sizeof(a[0]));
	printf("�z��x�̗v�f����%zu\n", sizeof(x) / sizeof(x[0]));

	return 0;
}
