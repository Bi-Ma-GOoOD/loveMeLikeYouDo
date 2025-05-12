#include <stdio.h>
//Compare max number
int compare(int *a, int *b){
    if(*a < *b) return *b;
    else return *a;
    return 0;
}
int main(){
    //Declare variables
    int first_number, second_number;
    //Input
    printf("Input the first number : ");
    scanf("%d",&first_number);
    printf("Input the second number : ");
    scanf("%d",&second_number);
    //Output
    printf("%d is maximum number.\n", compare(&first_number, &second_number));
}