// �O�̐����l��ǂݍ���ō��v�l�ƕ��ϒl��\��

#include <stdio.h>

int main(void)
{
	int a, b, c;

	puts("�O�̐�������͂���B");
	printf("����a�F");   scanf("%d", &a);
	printf("����b�F");   scanf("%d", &b);
	printf("����c�F");   scanf("%d", &c);

	int sum = a + b + c;				// ���v�l
	double ave = (double)sum / 3;		// ���ϒl�i�L���X�g���ŋ��߂�j

	printf("�����̍��v��%5d�ł��B\n",   sum);		// 99999�`���ŏo��
	printf("�����̕��ς�%5.1f�ł��B\n", ave);		// 999.9�`���ŏo��

	return 0;
}
