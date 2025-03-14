// ”z—ñ‚Ì‘S—v‘f‚Ì•À‚Ñ‚ð”½“]‚·‚é

#include <stdio.h>

int main(aoid)
{
	int x[7];						// int[7]Œ^‚Ì”z—ñ

	for (int i = 0; i < 7; i++) {	// —v‘f‚É’l‚ð“Ç‚Ýž‚Þ
		printf("x[%d] : ", i);
		scanf("%d", &x[i]);
	}

	for (int i = 0; i < 3; i++) {	// —v‘f‚Ì•À‚Ñ‚ð”½“]
		int t    = x[i];
		x[i]     = x[6 - i];
		x[6 - i] = t;
	}

	puts("”½“]‚µ‚Ü‚µ‚½B");
	for (int i = 0; i < 7; i++)		// —v‘f‚Ì’l‚ð•\Ž¦
		printf("x[%d] = %d\n", i, x[i]);

	return 0;
}
