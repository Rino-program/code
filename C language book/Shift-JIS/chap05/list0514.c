// �z��̗v�f�̂������̗v�f��ʂ̔z��ɃR�s�[

#include <stdio.h>

int main(void)
{
	int a[5];		// �R�s�[���z��
	int b[5];		// �R�s�[��z��

	for (int i = 0; i < 5; i++) {	// �v�f�ɒl��ǂݍ���
		printf("a[%d] : ", i);
		scanf("%d", &a[i]);
	}

	int count = 0;					// �R�s�[�����v�f��
	for (int i = 0; i < 5; i++)
		if (a[i] > 0)				// ���ł����
			b[count++] = a[i];		// �R�s�[

	for (int i = 0; i < count; i++)
		printf("b[%d] = %d\n", i, b[i]);

	return 0;
}
