#include <stdio.h>
#include <string.h>

int main(){
    char a = 'A';
    int i = 15;
    float f = 7.5;

    char *pt_a;
    int *pt_i;
    float *pt_f;

    pt_a = &a;
    pt_i = &i;
    pt_f = &f;

    printf("Address of a = %p, value of a = %c\n", pt_a, a);
    printf("Address of i = %p, value of i = %d\n", pt_i, i);
    printf("Address of f = %p, value of f = %.2f\n", pt_f, f);

    return 0;
}