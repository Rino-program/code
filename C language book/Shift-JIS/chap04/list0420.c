// ���������p�̒��p�񓙕ӎO�p�`��\��

#include <stdio.h>

int main(void)
{
	int len;

	puts("�������p�񓙕ӎO�p�`��\�����܂��B");
	printf("�Z�ӁF");
	scanf("%d", &len);

	for (int i = 1; i <= len; i++) {	// i�s�ii = 1, 2, �c , len�j
		for (int j = 1; j <= i; j++)	// �e�s��i��'*'��\��
			putchar('*');
		putchar('\n');					// ���s
	}

	return 0;
}
