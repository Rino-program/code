// �z��̑S�v�f��ʂ̔z��ɃR�s�[�i���j

#include <stdio.h>

int main(void)
{
	int a[5];		// �R�s�[���z��
	int b[5];		// �R�s�[��z��

	for (int i = 0; i < 5; i++) {	// �v�f�ɒl��ǂݍ���
		printf("a[%d] : ", i);
		scanf("%d", &a[i]);
	}

	b = a;			// �G���[�F�z��̑���͂ł��Ȃ�

	puts("  a    b");
	puts("---------");
	for (int i = 0; i < 5; i++)
		printf("%4d%4d\n", a[i], b[i]);

	return 0;
}
