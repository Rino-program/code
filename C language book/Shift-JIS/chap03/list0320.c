// �ǂݍ��񂾐����l���R�Ŋ�������]��\���iswitch���j

#include <stdio.h>

int main(void)
{
	int no;

	printf("�����l�F");
	scanf("%d", &no);

	switch (no % 3) {									// no % 3��
	 case 0 : puts("�R�Ŋ���؂�܂��B");		break;	// 0�ł���΁c
	 case 1 : puts("�R�Ŋ�������]�͂P�ł��B"); break;	// 1�ł���΁c
	 case 2 : puts("�R�Ŋ�������]�͂Q�ł��B"); break;	// 2�ł���΁c
	}

	return 0;
}
