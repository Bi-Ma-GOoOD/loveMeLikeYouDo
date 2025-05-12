#include <stdio.h>

int main(){
    //Declare variables
    int input, i;
    //Input
    printf("This is program about multiple table.\nSuch as\n\t2 * 1 = 2\n\t2 * 2 = 4\n");
    printf("Enter your number : ");
    scanf("%d", &input);
    //Process
    for(i = 1; i <= 12; i++){
        printf("%d x %d\t= %d\n", input, i, input * i);
    }
    return 0;
}