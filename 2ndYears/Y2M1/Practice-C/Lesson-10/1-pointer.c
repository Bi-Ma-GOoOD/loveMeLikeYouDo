#include <stdio.h>

int main(){
    int a = 2, b= 3;
    int *p = &a;

    printf("Pointer variable p points to variable a at address %p\n", p);
    printf("Value of a is %d, value of p is %d too\n", a, *p);
    p = &b;
    printf("Pointer variable p points to variable a at address %p\n", p);
    printf("Value of a is %d, value of p is %d too\n", b, *p);
}