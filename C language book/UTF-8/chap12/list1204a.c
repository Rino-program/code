// 学生の体重が不正であれば自動的に計算（アロー演算子）

#include <stdio.h>

#define NAME_LEN	64		// 名前の文字数

//=== 学生を表す構造体 ===//
struct student {
	char   name[NAME_LEN];	// 名前
	int    height;			// 身長
	double weight;			// 体重
};

//--- sが指す学生の体重が0以下であれば標準体重を代入 ---//
void set_stdweight(struct student *s)
{
	if (s->weight <= 0)
		s->weight = (s->height - 100) * 0.9;
}

int main(void)
{
	struct student takao = {"Takao", 173};

	set_stdweight(&takao);	// 標準体重を代入

	printf("氏名＝%s\n",   takao.name);
	printf("身長＝%d\n",   takao.height);
	printf("体重＝%.1f\n", takao.weight);

	return 0;
}
