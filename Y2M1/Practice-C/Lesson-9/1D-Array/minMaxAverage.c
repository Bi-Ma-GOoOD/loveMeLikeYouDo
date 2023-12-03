#include <stdio.h>

int main(){
    int num[5], i , max, min, sum = 0;
    float avg = 0.0;

    for(i = 0; i < 5; i++){
        num[i] = 0;
        printf("Enter number %d : ", i+1);
        scanf("%d", &num[i]);
    }
    max = num[0];
    min = num[0];

    for(i = 0; i < 5; i++)
        if(num[i] > max) max = num[i];
        else if(num[i] < min) min = num[i];
        sum += num[i];
    
    avg = (float)sum/5;
    printf("\nMax value is %d", max);
    printf("\nMin value is %d", min);
    printf("\nSum of your number is %d", sum);
    printf("\nAverage of your number is %.2f", avg);
}