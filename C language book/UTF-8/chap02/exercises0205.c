//演習2-5

#include <stdio.h>

int main(void){
    puts("整数を入力せよ。");
    double a, b;
    printf("整数a："); scanf("%lf", &a);
    printf("整数b："); scanf("%lf", &b);
    printf("aの値はbの%f%%です。\n", a / b * 100);
    return 0;
}