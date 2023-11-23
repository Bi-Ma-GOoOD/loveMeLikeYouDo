#include <stdio.h>
#include <string.h>

int main(){
    // Declare variables
    int storeNum[8];
    int firstMax, firstMin, secondMax, secondMin, i, j, temp;
    // UI
    printf("please enter seven integers number ( Ex. 1 2 3 4 5 6 7): ");
    scanf("%d %d %d %d %d %d %d", &storeNum[0], &storeNum[1], &storeNum[2], &storeNum[3], &storeNum[4], &storeNum[5], &storeNum[6]);
    // Buble sorting
    for(i = 0; i < 7; i++){
        for(j = i + 1; j < 7; j++){
            if(storeNum[j] < storeNum[i]){
                temp = storeNum[i];
                storeNum[i] = storeNum[j];
                storeNum[j] = temp;
            }
        }
    }
    //UI
    printf("First maximum number : %d\n", storeNum[7-1]);
    printf("Second maximum number : %d\n", storeNum[7-2]);
    printf("First minimum number : %d\n", storeNum[0]);
    printf("Second minimum number : %d\n", storeNum[1]);
}