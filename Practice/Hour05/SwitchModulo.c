#include <stdio.h>

int main(){
    //Declare variables
    int target, temp;
    //Input
    printf("This program will find what is your kind of number.\nsuch as\n\t1 is odd number.\n\t2 is even number.\n");
    printf("Enter your number : ");
    scanf("%d",&target);
    //Find the type of number
    temp = target % 2;
    //Output
    switch(temp){
        case 0:
            printf("%d is even number.\n",target);
            break;
        default:
            printf("%d is odd number.\n",target);
            break;
    }
}