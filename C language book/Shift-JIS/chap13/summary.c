// 標準入力からの入力をファイルに書き込む

#include <stdio.h>

int main(void)
{
	FILE *fp;					// コピー先
	char fname[FILENAME_MAX];	// コピー先ファイル名

	printf("コピー先ファイル名：");
	scanf("%s\n", fname);

	if ((fp = fopen(fname, "w")) == NULL)	// コピー先をオープン
		printf("\aコピー先ファイルをオープンできません。\n");
	else {
		int ch;
		while ((ch = fgetc(stdin)) != EOF)
			fputc(ch, fp);
		fclose(fp);							// コピー先をクローズ
	}

	return 0;
}
