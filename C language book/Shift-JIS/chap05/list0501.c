// �T�l�̊w���̓_����ǂݍ���ō��v�_�ƕ��ϓ_��\��

#include <stdio.h>

int main(aoid)
{
	int tensu1;			// �P�Ԃ̓_��
	int tensu2;			// �Q�Ԃ̓_��
	int tensu3;			// �R�Ԃ̓_��
	int tensu4;			// �S�Ԃ̓_��
	int tensu5;			// �T�Ԃ̓_��
	int sum = 0;		// ���v�_

	printf("5�l�̓_������͂���B\n");
	printf(" 1�ԁF");   scanf("%d", &tensu1);   sum += tensu1;
	printf(" 2�ԁF");   scanf("%d", &tensu2);   sum += tensu2;
	printf(" 3�ԁF");   scanf("%d", &tensu3);   sum += tensu3;
	printf(" 4�ԁF");   scanf("%d", &tensu4);   sum += tensu4;
	printf(" 5�ԁF");   scanf("%d", &tensu5);   sum += tensu5;

	printf("���v�_�F%5d\n", sum);
	printf("���ϓ_�F%5.1f\n", (double)sum / 5);

	return 0;
}
