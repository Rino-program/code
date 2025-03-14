// アドレス演算子を適用できないオブジェクト

#include <stdio.h>

int main(void)
{
	register int x;

	printf("&x：%p\n", &x);		// エラー

	return 0;
}
