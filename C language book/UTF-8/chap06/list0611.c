// 英語の点数と数学の点数の最高点を求める

#include <stdio.h>

#define NUMBER	5		// 学生の人数

//--- 要素数nの配列vの最大値を返す ---//
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
	int eng[NUMBER];		// 英語の点数
	int mat[NUMBER];		// 数学の点数

	printf("%d人の点数を入力せよ。\n", NUMBER);
	for (int i = 0; i < NUMBER; i++) {
		printf("[%d] 英語：", i + 1);  scanf("%d", &eng[i]);
		printf( "    数学：");         scanf("%d", &mat[i]);
	}
	int max_e = max_of(eng, NUMBER);	// 英語の最高点
	int max_m = max_of(mat, NUMBER);	// 数学の最高点

	printf("英語の最高点＝%d\n", max_e);
	printf("数学の最高点＝%d\n", max_m);

	return 0;
}
