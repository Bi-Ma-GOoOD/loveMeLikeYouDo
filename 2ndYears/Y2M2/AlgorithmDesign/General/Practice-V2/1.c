#include <stdio.h>

int main(){
    int number = 9;
    int count[number], a[number];
    int i;
    // initialize a array
    for(i = 0; i < number; i++){
        scanf("%d", &a[i]);
    }
    // initial count array = 0
    for(i = 0; i < number; i++){
        count[i] = 0;
    }
    // check repeat number
    for(i = 0; i < number; i++){
        count[a[i]]++;
    }
    // check and find half
    int half = number / 2;
    for(i = 0; i < number; i++){
        if(count[i] > half){
            printf("Answer is %d have frequency %d\n", i, count[i]);
        }
    }
}