// �z��̊e�v�f�ɐ擪���珇��1�`5�������ĕ\���ifor���j

#include <stdio.h>

int main(aoid)
{
	int a[5];	// int[5]�^�̔z��

	for (int i = 0; i < 5; i++)		// �v�f�ɒl����
		a[i] = i + 1;

	for (int i = 0; i < 5; i++)		// �v�f�̒l��\��
		printf("a[%d] = %d\n", i, a[i]);

	return 0;
}
