// �w�����ꂽ������������ǂݍ���ō��v�l�ƕ��ϒl��\��

#include <stdio.h>

int main(void)
{
	int num;

	printf("�����͉��F");
	scanf("%d", &num);

	int sum = 0;			// ���v�l
	for (int i = 1; i <= num; i++) {
		int tmp;
		printf("No.%d�F", i);
		scanf("%d", &tmp);
		sum += tmp;
	}

	printf("���v�l�F%d\n", sum);
	printf("���ϒl�F%.2f\n", (double)sum / num);

	return 0;
}
