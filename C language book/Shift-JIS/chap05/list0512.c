// �w���̓_����ǂݍ���ŕ��z��\��

#include <stdio.h>

#define NUMBER	120		// �l���̏��

int main(void)
{
	int num;				// ���ۂ̐l��
	int tensu[NUMBER];		// �w���̓_��
	int bunpu[11] = {0};	// �_���̕��z

	printf("�l������͂���F");

	do {
		scanf("%d", &num);
		if (num < 1 || num > NUMBER)
			printf("\a1�`%d�œ��͂���F", NUMBER);
	} while (num < 1 || num > NUMBER);

	printf("%d�l�̓_������͂���B\n", num);

	for (int i = 0; i < num; i++) {
		printf("%2d�ԁF", i + 1);
		do {
			scanf("%d", &tensu[i]);
			if (tensu[i] < 0 || tensu[i] > 100)
				printf("\a0�`100�œ��͂���F");
		} while (tensu[i] < 0 || tensu[i] > 100);
		bunpu[tensu[i] / 10]++;
	}

	puts("\n---���z�O���t---");
	printf("      100�F");

	for (int j = 0; j < bunpu[10]; j++)			// 100�_
		putchar('*');
	putchar('\n');

	for (int i = 9; i >= 0; i--) {				// 100�_����
		printf("%3d �`%3d�F", i * 10, i * 10 + 9);
		for (int j = 0; j < bunpu[i]; j++)
			putchar('*');
		putchar('\n');
	}

	return 0;
}
