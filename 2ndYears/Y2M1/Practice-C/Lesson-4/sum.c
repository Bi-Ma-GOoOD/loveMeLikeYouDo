#include <stdio.h>
#include <math.h>

void sum(int number);

int main(){
    int end;

    printf("Enter your end number to sum: ");
    scanf("%d", &end);
    sum(end);
}

void sum(int number){
    int sum = 0; 

    for(int i = 1; i <= number; i++)
        sum += i;
    printf("Sum = %d", sum);
}