// •¶š—ñ‚Ì”z—ñ‚ğ“Ç‚İ‚ñ‚Å•\¦

#include <stdio.h>

int main(void)
{
	char s[3][128];

	for (int i = 0; i < 3; i++) {
		printf("s[%d] : ", i);
		scanf("%s", s[i]);
	}

	for (int i = 0; i < 3; i++)
		printf("s[%d] = \"%s\"\n", i, s[i]);

	return 0;
}
