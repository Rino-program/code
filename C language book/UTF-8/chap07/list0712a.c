// 0.0から1.0まで0.01単位で繰り返す（for文の制御式を!=演算子に変更）

#include <stdio.h>

int main(void)
{
	for (float x = 0.0; x != 1.0; x += 0.01)
		printf("x = %f\n", x);

	return 0;
}
