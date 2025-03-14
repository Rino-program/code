// 指示された個数だけ整数を読み込んで合計値と平均値を表示

#include <stdio.h>

int main(void)
{
	int num;

	printf("整数は何個：");
	scanf("%d", &num);

	int i = 0;
	int sum = 0;			// 合計値
	while (i < num) {
		int tmp;
		printf("No.%d：", ++i);		// iの値をインクリメントした後に表示
		scanf("%d", &tmp);
		sum += tmp;
	}

	printf("合計値：%d\n", sum);
	printf("平均値：%.2f\n", (double)sum / num);

	return 0;
}
