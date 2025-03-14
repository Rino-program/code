// •¶Žš—ñ‚Ì”z—ñ

#include <stdio.h>

int main(void)
{
	char s[][6] = {"Turbo", "NA", "DOHC"};

	for (int i = 0; i < 3; i++)
		printf("s[%d] = \"%s\"\n", i, s[i]);

	return 0;
}
