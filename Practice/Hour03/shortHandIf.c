#include <stdio.h>

int main(){
    //Declare variables
    int current;
    int time = 12;
    //Input
    printf("Enter your integer time : ");
    scanf("%d",&current);
    //Output
    (current < 12) ? printf("Good Morning\t^.^\n") : printf("Good Afternoon\t^.^\n");
}