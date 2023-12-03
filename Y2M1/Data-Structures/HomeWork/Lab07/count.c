#include <stdio.h>

int checkCount(int array[], int amountNumber, int checkNumber);

int main(){
    int amount;
    int numberCheck;

    // printf("Enter amount: ");
    scanf("%d", &amount);

    int arrayNum[amount];
    for(int i = 0; i < amount; ++i){
        // printf("Enter number[%d]: ", i+1);
        scanf("%d", &arrayNum[i]);
    }

    // printf("Enter number check: ");
    scanf("%d", &numberCheck);
    int answer = checkCount(arrayNum, amount, numberCheck);
    // printf("Answer: %d", answer);
    printf(" %d", answer);
}

int checkCount(int array[], int amountNumber, int checkNumber){
    int count = 0;
    
    for(int i = 0; i < amountNumber; ++i){
        if(array[i] == checkNumber){
            count++;
        }else{
            continue;
        }
    }
    return count;
}