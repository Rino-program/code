// �ǂݍ��񂾓�̐����l�̑傫���ق��̒l��\���i���̂R�F�������Z�q�j

#include <stdio.h>

int main(void)
{
	int n1, n2;

	puts("��̐�������͂���B");
	printf("�����P�F");   scanf("%d", &n1);
	printf("�����Q�F");   scanf("%d", &n2);

	int max = n1 > n2 ? n1 : n2;		// �傫���ق��̒l��max��������

	printf("�傫���ق��̒l��%d�ł��B\n", max);

	return 0;
}
