// �p��̓_���Ɛ��w�̓_���̍ō��_�����߂�

#include <stdio.h>

#define NUMBER	5		// �w���̐l��

//--- �v�f��n�̔z��v�̍ő�l��Ԃ� ---//
int max_of(int v[], int n)
{
	int max = v[0];

	for (int i = 1; i < n; i++)
		if (v[i] > max)
			max = v[i];
	return max;
}

int main(void)
{
	int eng[NUMBER];		// �p��̓_��
	int mat[NUMBER];		// ���w�̓_��

	printf("%d�l�̓_������͂���B\n", NUMBER);
	for (int i = 0; i < NUMBER; i++) {
		printf("[%d] �p��F", i + 1);  scanf("%d", &eng[i]);
		printf( "    ���w�F");         scanf("%d", &mat[i]);
	}
	int max_e = max_of(eng, NUMBER);	// �p��̍ō��_
	int max_m = max_of(mat, NUMBER);	// ���w�̍ō��_

	printf("�p��̍ō��_��%d\n", max_e);
	printf("���w�̍ō��_��%d\n", max_m);

	return 0;
}
