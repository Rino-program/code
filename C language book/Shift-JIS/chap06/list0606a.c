// ‚×‚«æ‚ğ‹‚ß‚éidoubleŒ^‰¼ˆø”‚ÉintŒ^Àˆø”‚ğ—^‚¦‚éj

#include <stdio.h>

//--- x‚Ìnæ‚ğ•Ô‚· ---//
double power(double x, int n)
{
	double tmp = 1.0;

	while (n-- > 0)
		tmp *= x;	// tmp‚Éx‚ğŠ|‚¯‚é
	return tmp;
}

int main(void)
{
	printf("5‚Ì3æ‚Í%.2f‚Å‚·B\n", power(5, 3));

	return 0;
}
