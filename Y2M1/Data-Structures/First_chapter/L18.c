#include <stdio.h>

int main(){
    int score[10];
    float sum = 0;
    for(int i = 0; i < 10; i++){
        printf("Enter score[%d]: ",i);
        scanf("%d",&score[i]);
        sum += score[i];
    }
    printf("Average score: %.2f\n",sum/10);
    return 0;
}