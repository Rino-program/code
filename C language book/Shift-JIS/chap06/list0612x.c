// �z��̑S�v�f���[���ɂ���i���j

#include <stdio.h>

//--- �v�f��n�̔z��v�̗v�f��0���� ---//
// �G���[�Fconst�錾���Ă͂Ȃ�Ȃ�
void set_zero(const int v[], int n)
{
	for (int i = 0; i < n; i++)
		v[i] = 0;
}

//--- �v�f��n�̔z��v�̑S�v�f��\�����ĉ��s ---//
void print_array(const int v[], int n)
{
	v[1] = 5;	// �G���[�Fconst�錾���ꂽ�z��̗v�f�ɂ͑���ł��Ȃ�
	printf("{ ");
	for (int i = 0; i < n; i++)
		printf("%d ", v[i]);
	printf("}\n");
}

int main(void)
{
	int ary1[] = {1, 2, 3, 4, 5};
	int ary2[] = {3, 2, 1};

	printf("ary1 = ");   print_array(ary1, 5);
	printf("ary2 = ");   print_array(ary2, 3);

	set_zero(ary1, 5);		// �z��ary1�̑S�v�f��0����
	set_zero(ary2, 3);		// �z��ary2�̑S�v�f��0����

	printf("���z��̑S�v�f��0�������܂����B\n");
	printf("ary1 = ");   print_array(ary1, 5);
	printf("ary2 = ");   print_array(ary2, 3);

	return 0;
}
