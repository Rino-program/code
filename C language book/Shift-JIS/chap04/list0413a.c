// �ǂݍ��񂾐����̌���������A���\���ifor���Fi�̊J�n��1�j

#include <stdio.h>

int main(void)
{
	int no;

	printf("���̐����F");
	scanf("%d", &no);

	for (int i = 0; i < no; i++)
		putchar('*');
	putchar('\n');

	return 0;
}
