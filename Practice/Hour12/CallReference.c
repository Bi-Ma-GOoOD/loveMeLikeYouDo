#include <stdio.h>
//Adding functions call by reference
int add(int *first, int *second, int *sum){
    *sum = *first + *second;
    return 0;
}
int main(){
    int first_number, second_number, sum = 0;
    //Input
    printf("Enter the first number : ");
    scanf("%d",&first_number);
    printf("Enter the second number : ");
    scanf("%d",&second_number);
    //Process
    add(&first_number, &second_number, &sum);
    //Output
    printf("The sum of %d and %d is %d\n", first_number, second_number, sum);
    return 0;
}