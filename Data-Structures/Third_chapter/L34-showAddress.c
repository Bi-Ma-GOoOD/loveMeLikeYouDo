#include <stdio.h>
#include <conio.h>

int main(){
    int i;
    int *ptr_i;

    i = 3;
    ptr_i = &i;

    printf("Address of i = %p\n", &i);
    printf("value of ptr_i = %p\n", ptr_i);
    printf("value of i = %d\n", i);
    printf("value of *ptr_i = %d\n", *ptr_i);
    printf("Comparing the varaible belows\n");
    printf("&*ptr_i = %p\n", &*ptr_i);
    printf("*&ptr_i = %p\n", *&ptr_i);
}