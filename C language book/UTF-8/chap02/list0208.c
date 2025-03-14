// 型と演算の確認

#include <stdio.h>

int main(void)
{
	int    n1, n2, n3, n4;	// 整数
	double d1, d2, d3, d4;	// 浮動小数点数

	n1 = 15   / 2;			// n1 ← 7  
	n2 = 15.0 / 2.0;		// n2 ← 7.5（代入時に小数部を切捨て）
	n3 = 15.0 / 2;			// n3 ← 7.5（代入時に小数部を切捨て）
	n4 = 15   / 2.0;		// n4 ← 7.5（代入時に小数部を切捨て）

	d1 = 15   / 2;			// d1 ← 7   
	d2 = 15.0 / 2.0;		// d2 ← 7.5 
	d3 = 15.0 / 2;			// d3 ← 7.5 
	d4 = 15   / 2.0;		// d4 ← 7.5 

	printf("n1 = %d\n", n1);
	printf("n2 = %d\n", n2);
	printf("n3 = %d\n", n3);
	printf("n4 = %d\n\n", n4);

	printf("d1 = %f\n", d1);
	printf("d2 = %f\n", d2);
	printf("d3 = %f\n", d3);
	printf("d4 = %f\n", d4);

	return 0;
}
