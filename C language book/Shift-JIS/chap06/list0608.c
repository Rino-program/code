// �E�����p�̒��p�񓙕ӎO�p�`��\���i�֐��Łj

#include <stdio.h>

//--- ����ch��n�A�����ĕ\�� ---//
void put_chars(int ch, int n)
{
	while (n-- > 0)
		putchar(ch);
}

int main(void)
{
	int len;

	printf("�E�����p�񓙕ӎO�p�`�����܂��B\n");
	printf("�Z�ӁF");
	scanf("%d", &len);

	for (int i = 1; i <= len; i++) {
		put_chars(' ', len - i);
		put_chars('*', i);
		putchar('\n');
	}

	return 0;
}
