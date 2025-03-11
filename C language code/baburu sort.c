// バブルソート
# include <stdio.h>
# include <stdlib.h>

void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void buburu_sort(int *array, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = n - 1; j > i; j--) {
            if (array[j] < array[j - 1]) {
                swap(&array[j], &array[j - 1]);
            }
        }
    }
}

int main() {
    int n = 10;
    int *array = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) {
        array[i] = rand() % 100;
    }
    printf("ソート前：");
    for (int i = 0; i < n; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
    buburu_sort(array, n);
    printf("ソート後：");
    for (int i = 0; i < n; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
    free(array);
    return 0;
}