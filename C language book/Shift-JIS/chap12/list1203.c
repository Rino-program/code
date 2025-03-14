// 学生を表す構造体（メンバを初期化）

#include <stdio.h>

#define NAME_LEN	64		// 名前の文字数

//=== 学生を表す構造体 ===//
struct student {
	char   name[NAME_LEN];	// 名前
	int    height;			// 身長
	double weight;			// 体重
};

int main(void)
{
	struct student takao = {"Takao", 173};

	printf("氏名＝%s\n",   takao.name);
	printf("身長＝%d\n",   takao.height);
	printf("体重＝%.1f\n", takao.weight);

	return 0;
}
