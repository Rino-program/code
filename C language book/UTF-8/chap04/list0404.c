﻿// 整数値を次々と読み込んで合計と平均を表示（その２）

#include <stdio.h>

int main(void)
{
	int sum = 0;	// 合計
	int cnt = 0;	// 整数値の個数
	int retry;		// 処理を続けるか

	do {
		int t;

		printf("整数値を入力せよ：");
		scanf("%d", &t);

		sum += t;	 // sumにtを加える
		cnt++;		 // cntをインクリメントする（値を１増やす）

		printf("まだ？<Yes…0/No…9>：");
		scanf("%d", &retry);
	} while (retry == 0);

	printf("合計は%dで平均は%.2fです。\n", sum, (double)sum / cnt);

	return 0;
}
