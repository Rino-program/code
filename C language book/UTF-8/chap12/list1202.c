// 学生を表す構造体（メンバに値を代入／コピー）

#include <stdio.h>
#include <string.h>

#define NAME_LEN	64		// 名前の文字数

//=== 学生を表す構造体 ===//
struct student {
	char   name[NAME_LEN];	// 名前
	int    height;			// 身長
	double weight;			// 体重
};

int main(void)
{
	struct student sanaka;

	strcpy(sanaka.name, "Sanaka");	// 名前
	sanaka.height = 175;			// 身長
	sanaka.weight = 62.5;			// 体重

	printf("氏名＝%s\n",   sanaka.name);
	printf("身長＝%d\n",   sanaka.height);
	printf("体重＝%.1f\n", sanaka.weight);

	return 0;
}
