// �ǂݍ��񂾐����̌���������A���\���ifor���j

#include <stdio.h>

int main(void)
{
	int no;

	printf("���̐����F");
	scanf("%d", &no);

	for (int i = 1; i <= no; i++)
		putchar('*');
	putchar('\n');

	return 0;
}
