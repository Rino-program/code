// 標準入力からの入力を標準出力にコピーする

#include <stdio.h>

int main(void)
{
	int ch;

	while (1) {				// 無限ループ
		ch = getchar();		// 読み込んだ文字をchに代入
		if (ch == EOF)		// エラーが発生したら
			break;			// while文を強制的に抜け出す
		putchar(ch);		// 文字chを表示
	}

	return 0;
}
