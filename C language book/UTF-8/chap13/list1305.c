// ファイルの中身を表示する

#include <stdio.h>

int main(void)
{
	FILE *fp;
	char fname[FILENAME_MAX];	// ファイル名

	printf("ファイル名：");
	scanf("%s", fname);

	if ((fp = fopen(fname, "r")) == NULL)					// オープン
		printf("\aファイルをオープンできません。\n");
	else {
		int ch;
		while ((ch = fgetc(fp)) != EOF)
			putchar(ch);
		fclose(fp);											// クローズ
	}

	return 0;
}
