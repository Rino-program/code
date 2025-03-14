// putchar関数とprintf関数の誤用例（エラー）

#include <stdio.h>

int main(void)
{
	putchar("A");	// エラー：putcharに渡すのは文字。  正しくはputchar('A');
	printf('A');	// エラー：printf に渡すのは文字列。正しくはprintf("A"); 

	return 0;
}
