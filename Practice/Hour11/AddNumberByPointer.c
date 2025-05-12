#include <stdio.h>

int main(){
    //Declare variables
    int f, s;
    int *p_f = &f, *p_s = &s;
    //Input
    printf("Input the first number : ");
    scanf("%d", &f);
    printf("Input the second number : ");
    scanf("%d", &s);
    printf("The sum of the entered numbers is : %d\n", (*p_f + *p_s));
}