// strlenŠÖ”‚Ì—˜—p—á

#include <stdio.h>
#include <string.h>

int main(void)
{
	char str[128];

	printf("•¶š—ñF");
	scanf("%s", str);

	printf("•¶š—ñ\"%s\"‚Ì’·‚³‚Í%zu‚Å‚·B\n", str, strlen(str));

	return 0;
}
