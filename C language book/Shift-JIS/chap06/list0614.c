// ’€Ÿ’Tõi”Ô•º–@j

#include <stdio.h>

#define NUMBER		5		// —v‘f”
#define FAILED		-1		// ’Tõ¸”s

//--- —v‘f”n‚Ì”z—ñv‚©‚çkey‚Æˆê’v‚·‚é—v‘f‚ğ’Tõi”Ô•º–@j---//
int search(int v[], int key, int n)
{
	int i = 0;

	v[n] = key;		// ”Ô•º‚ğŠi”[

	while (1) {
		if (v[i] == key)
			break;			// ’Tõ¬Œ÷
		i++;
	}
	return i < n ? i : FAILED;
}

int main(void)
{
	int ky, idx;
	int x[NUMBER + 1];

	for (int i = 0; i < NUMBER; i++) {
		printf("x[%d]F", i);
		scanf("%d", &x[i]);
	}
	printf("’T‚·’lF");
	scanf("%d", &ky);

	if ((idx = search(x, ky, NUMBER)) == FAILED)
		puts("\a’Tõ‚É¸”s‚µ‚Ü‚µ‚½B");
	else
		printf("%d‚Í%d”Ô–Ú‚É‚ ‚è‚Ü‚·B\n", ky, idx + 1);

	return 0;
}
