// �ǂݍ��񂾓�̐����l�̑傫���ق��̒l��\���i���̂Q�j

#include <stdio.h>

int main(void)
{
	int n1, n2;

	puts("��̐�������͂���B");
	printf("�����P�F");   scanf("%d", &n1);
	printf("�����Q�F");   scanf("%d", &n2);

	int max;
	if (n1 > n2) max = n1; else max = n2;
	printf("�傫���ق��̒l��%d�ł��B\n", max);

	return 0;
}
