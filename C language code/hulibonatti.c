// フィボナッチ数列

#include <stdio.h>

int fib(int n) {
    if (n == 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
        return fib(n - 1) + fib(n - 2);
    }
}

int main() {
    int n = 10;
    printf("フィボナッチ数列 %d 桁：", n);
    for (int i = 0; i <= n; i++) {
        printf("%d ", fib(i));
    }
    printf("\n");
    return 0;
}