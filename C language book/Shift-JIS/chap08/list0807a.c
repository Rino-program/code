// KćđÄAIÉßéiđZqj

#include <stdio.h>

//--- ŽlnĚKćlđÔpiđZqj ---//
int factorial(int n)
{
	return n > 0 ? n * factorial(n - 1) : 1;
}

int main(void)
{
	int num;

	printf("ŽđüÍšćF");
	scanf("%d", &num);

	printf("%dĚKćÍ%dĹˇB\n", num, factorial(num));

	return 0;
}
