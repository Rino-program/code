//演習2-2
# include <stdio.h>
int main(void){
    int a, b;
    puts("二つの整数を入力せよ。");
    printf("整数a："); scanf("%d", &a);
    printf("整数b："); scanf("%d", &b);
    printf("それらの和は%dで積は%dです。\n", a + b, a * b);
    return 0;
}