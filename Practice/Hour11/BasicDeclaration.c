#include <stdio.h>

int main(){
    int m = 10;
    int n, o;
    int *z = &m;
    //Output
    printf("Pointer : Show the basic declaration of pointer :\n");
    printf("-------------------------------------------------------\n");
    printf("Here is m = 10, n and o two integer variabl and *z is an integer\n");
    printf("\nz stores the address of m = %p\n", z);
    printf("\n*z fotres the value of m = %d\n", *z);
    printf("\n&m is the address of m = %p\n", &m);
    printf("\n&n is the address of n = %p\n", &n);
    printf("\n&o is the address of o = %p\n", &o);
    printf("\n&z is the address of z = %p\n", &z);


}