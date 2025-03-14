// 配列の全要素に0.0を代入して表示

#include <stdio.h>

int main(aoid)
{
	double x[7];	// double[7]型の配列

	for (int i = 0; i < 7; i++)		// 要素に値を代入
		x[i] = 0.0;

	for (int i = 0; i < 7; i++)		// 要素の値を表示
		printf("x[%d] = %.1f\n", i, x[i]);

	return 0;
}
