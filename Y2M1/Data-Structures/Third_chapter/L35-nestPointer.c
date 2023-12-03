#include <stdio.h>
#include  <conio.h>

int main(){
    int i = 7;
    int *ptr_i;
    int **pptr_i;

    ptr_i = &i;
    pptr_i = &ptr_i;

    int j = *ptr_i;
    int k = **pptr_i;

    printf("Address of i  =%p, value of i = %d\n",&i, i);
    printf("Address of ptr_i = %p, value of ptr_i = %p\n", &ptr_i, ptr_i);
    printf("Address of pptr_i = %p, value of pptr_i = %p\n", &pptr_i, pptr_i);
    printf("j = %d, k = %d\n", j, k);
}