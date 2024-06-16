#include <stdio.h>

int plus(int ptr_a, int ptr_b){
    int sum = ptr_a + ptr_b;
    return sum;
}

int main(){
    //Declare variables
    int a = 4;
    int b = 16;
    int *ptr_a = &a;
    int *ptr_b = &b;
    //Input
    // printf("Welcome to plus!\n");
    // printf("Enter a number : ");
    // scanf("%d", &a);
    // printf("Enter b number : ");
    // scanf("%d", &b);
    //Process
    int result = plus(*ptr_a, *ptr_b);
    printf("%d", result);
}