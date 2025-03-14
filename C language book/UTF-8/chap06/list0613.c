// 線形探索（逐次探索）

#include <stdio.h>

#define NUMBER		5		// 要素数
#define FAILED		-1		// 探索失敗

//--- 要素数nの配列vからkeyと一致する要素を探索 ---//
int search(const int v[], int key, int n)
{
	int i = 0;

	while (1) {
		if (i == n)
			return FAILED;		// 探索失敗
		if (v[i] == key)
			return i;			// 探索成功
		i++;
	}
}

int main(void)
{
	int ky, idx;
	int x[NUMBER];

	for (int i = 0; i < NUMBER; i++) {
		printf("x[%d]：", i);
		scanf("%d", &x[i]);
	}
	printf("探す値：");
	scanf("%d", &ky);

	idx = search(x, ky, NUMBER);	// 要素数NUMBERの配列xからkyを探索

	if (idx == FAILED)
		puts("\a探索に失敗しました。");
	else
		printf("%dは%d番目にあります。\n", ky, idx + 1);

	return 0;
}
