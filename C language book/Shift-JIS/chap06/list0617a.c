// ���ʎq�̗L���͈͂��m�F����i�s���j

#include <stdio.h>

int x = 75;						// �`�t�@�C���L���͈�

void print_x(void)
{
	printf("x = %d\n", x);
}

int main(void)
{
	int i;
	// x�����g�̕s��l�ŏ�����
	int x = x;					// �a�u���b�N�L���͈�

	print_x();

	printf("x = %d\n", x);

	for (i = 0; i < 5; i++) {
		int x = i * 100;		// �b�u���b�N�L���͈�
		printf("x = %d\n", x);
	}

	printf("x = %d\n", x);

	return 0;
}
