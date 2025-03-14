// ５人の学生を身長の昇順にソート

#include <stdio.h>
#include <string.h>

#define NUMBER		5		// 学生の人数
#define NAME_LEN	64		// 名前の文字数

//=== 学生を表す構造体 ===//
typedef struct {
	char   name[NAME_LEN];	// 名前
	int    height;			// 身長
	double weight;			// 体重
} Student;

//--- xおよびyが指す学生を交換 ---//
void swap_Student(Student *x, Student *y)
{
	Student temp = *x;
	*x = *y;
	*y = temp;
}

//--- 学生の配列aの先頭n個の要素を身長の昇順にソート ---//
void sort_by_height(Student a[], int n)
{
	for (int i = 0; i < n - 1; i++) {
		for (int j = n - 1; j > i; j--)
			if (a[j - 1].height > a[j].height)
				swap_Student(&a[j - 1], &a[j]);
	}
}

int main(void)
{
	Student std[] = {
		{"Sato",   178, 61.2},		// 佐藤君
		{"Sanaka", 175, 62.5},		// 佐中君
		{"Takao",  173, 86.2},		// 高尾君
		{"Mike",   165, 72.3},		// Mike君
		{"Masaki", 179, 77.5},		// 真崎君
	};

	for (int i = 0; i < NUMBER; i++)
		printf("%-8s %6d%6.1f\n", std[i].name, std[i].height, std[i].weight);

	sort_by_height(std, NUMBER);	// 身長の昇順にソート

	puts("\n身長順にソートしました。");
	for (int i = 0; i < NUMBER; i++)
		printf("%-8s %6d%6.1f\n", std[i].name, std[i].height, std[i].weight);

	return 0;
}
