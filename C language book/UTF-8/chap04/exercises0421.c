//演習4-21
# include <stdio.h>

int main(void){
    puts("正方形を作ります。");
    int n;
    printf("何段ですか："); scanf("%d", &n);
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            putchar('*');
        }
        putchar('\n');
    }
    return 0;
}