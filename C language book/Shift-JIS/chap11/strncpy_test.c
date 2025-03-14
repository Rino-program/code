// strncpy関数の利用例（バグにつながりかねない例）

#include <stdio.h>
#include <string.h>

int main(void)
{
	char s1[5] = {'X', 'X', 'X', 'X', 'X'};
	strncpy(s1, "12345", 2);

	printf("s1 = %s\n", s1);	// s1は文字列ではないので正しく表示できない

	return 0;
}
