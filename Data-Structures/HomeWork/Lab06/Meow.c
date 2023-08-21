#include <stdio.h>

void checkMeow(char numString[]);

int main(){
    int loop, numString, i;

    printf("Input Round: ");
    scanf("%d",&loop);

    for(i = 0; i < loop; ++i){
        printf("Input number of strings: ");
        scanf("%d",&numString);

        char string[numString];
        printf("Input String: ");
        scanf("%s",string);
    }
    checkMeow(numString);
}

void checkMeow(char numString[]){
    
}