#include <stdio.h>

int main(){
    int i = 7, j;
    float f = 2.5;
    char c = 'C', d;

    int *ptr_i;
    float *ptr_f;
    char *ptr_c;

    ptr_i = &i;
    ptr_f = &f;
    ptr_c = &c;

    j = *ptr_i;
    d = *ptr_c;

    printf("value of i = %d\n", i);
    printf("value of f = %.2f\n", f);
    printf("value of d = %c\n", d);
    
    return 0;
}