// �ǂݍ��񂾓�̐����l�̘a�i���Z���ʁj��ϐ��Ɋi�[���ĕ\��

#include <stdio.h>

int main(void)
{
	int n1, n2;

	puts("��̐�������͂��Ă��������B");
	printf("����n1�F");   scanf("%d", &n1);
	printf("����n2�F");   scanf("%d", &n2);

	int wa = n1 + n2;						// n1��n2�̘a��wa��������

	printf("�����̘a��%d�ł��B\n", wa);		// �a��\��
	printf("���Ȃ킿n1 + n2 = %d�ł��B\n", wa);	// �a��\��

	return 0;
}
