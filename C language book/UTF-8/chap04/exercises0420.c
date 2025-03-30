//演習4-20
# include <stdio.h>

int main(void){
    puts("   | 1  2  3  4  5  6  7  8  9");
    puts("---+---------------------------");
    for(int i = 1; i <= 9; i++){
        printf("%d  |", i);
        for(int j = 1; j <= 9; j++){
            printf("%2d", i * j);
            if(j == 9){
                putchar('\n');
            }else{
                putchar(' ');
            }
        }
    }
}