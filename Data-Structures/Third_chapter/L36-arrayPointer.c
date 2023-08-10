#include <stdio.h>

int main(){
    int i, offset;
    int a[] = {10, 20, 30, 40};
    int *ptr_a = a;

    for(i = 0; i < 4; i++){
        printf("a[%d] = %d\n", i, a[i]);
        printf("*(a + %d)  = %d\n", i, *(a+i));
        printf("(a + %d)  = %d\n", i, a+i);
        printf("ptr_a[%d] = %d\n", i, ptr_a[i]);
        printf("*(ptr_a + %d) = %d\n\n", i, *(ptr_a + i));
    }
    return 0;
}