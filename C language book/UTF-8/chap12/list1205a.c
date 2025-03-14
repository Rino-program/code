// 構造体にtypedef名を与えメンバの値をキーボードから読み込む（タグ名を与えない）

#include <stdio.h>

#define NAME_LEN	64		// 名前の文字数

//=== 学生を表す構造体 ===//
typedef struct {
	char   name[NAME_LEN];	// 名前
	int    height;			// 身長
	double weight;			// 体重
} Student;

int main(void)
{
	Student takao;

	printf("氏名：");  scanf("%s",  takao.name);
	printf("身長：");  scanf("%d",  &takao.height);
	printf("体重：");  scanf("%lf", &takao.weight);

	printf("氏名＝%s\n",   takao.name);
	printf("身長＝%d\n",   takao.height);
	printf("体重＝%.1f\n", takao.weight);

	return 0;
}
