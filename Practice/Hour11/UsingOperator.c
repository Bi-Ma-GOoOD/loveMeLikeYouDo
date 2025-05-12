#include <stdio.h>

int main(){
    int m = 300;
    float fx = 300.600006;
    char cht = 'z';
    int *ptr_m = &m;
    float *ptr_fx = &fx;
    char *ptr_cht = &cht;
    //Output
    printf("Pointer : Demostrate the use of & and * operator :\n");
    printf("-------------------------------------------------------\n");
    printf("m = %d\n", m);
    printf("fx = %.6f\n", fx);
    printf("cht = %c\n", cht);
    printf("\nUsing & operator : \n");
    printf("-----------------------\n");
    printf("address of m = %p\n", &m);
    printf("address of fx = %p\n", &fx);
    printf("address of cht = %p\n", &cht);
    printf("\nUsing & and * operator : \n");
    printf("-----------------------------\n");
    printf("value at address of m = %d\n", *ptr_m);
    printf("value at address of fx = %.6f\n", *ptr_fx);
    printf("value at address of cht = %c\n", *ptr_cht);
    printf("\nUsing only pointer variable : \n");
    printf("----------------------------------\n");
    printf("address of m = %p\n", ptr_m);
    printf("address of fx = %p\n", ptr_fx);
    printf("address of cht = %p\n", ptr_cht);
    printf("\nUsing only pointer operator :\n");
    printf("----------------------------------\n");
    printf("value at address of m = %d\n", *ptr_m);
    printf("value at address of fx = %.6f\n", *ptr_fx);
    printf("value at address of cht = %c\n", *ptr_cht);
}