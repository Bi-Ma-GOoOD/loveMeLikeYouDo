#include <stdio.h>

int main(){
    int i = 7;
    int j;
    int k[10];
    int *ptr;
    k[0] = 1;
    ptr = &i;

    printf("Address of i = %p, value of i = %d\n",ptr, i);
    j = *ptr;
    printf("j = %d\n", j);
    j = 10;
    printf("i = %d\n", i);
    printf("j = %d\n", j);
    *ptr = 0;
    printf("value of ptr = %p, value of *ptr = %d\n", ptr, *ptr);
    ptr = &k[0];
    printf("value of ptr = %p, value of *ptr = %d\n", ptr, *ptr);
    return 0;
}