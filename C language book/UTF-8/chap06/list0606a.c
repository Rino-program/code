// べき乗を求める（double型仮引数にint型実引数を与える）

#include <stdio.h>

//--- xのn乗を返す ---//
double power(double x, int n)
{
	double tmp = 1.0;

	while (n-- > 0)
		tmp *= x;	// tmpにxを掛ける
	return tmp;
}

int main(void)
{
	printf("5の3乗は%.2fです。\n", power(5, 3));

	return 0;
}
