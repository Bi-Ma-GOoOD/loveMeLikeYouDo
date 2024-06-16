#include <stdio.h>

int plus(int *ptr_a, int *ptr_b){
    int sum = *ptr_a + *ptr_b;
    return sum;
}

int main(){
    //Declare variables
    int a;
    int b;
    //Input
    printf("Welcome to plus!\n");
    printf("Enter a number : ");
    scanf("%d", &a);
    printf("Enter b number : ");
    scanf("%d", &b);
    //Process
    int result = plus(&a, &b);
    printf("%d", result);
}