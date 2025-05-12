#include <stdio.h>

int main(){
    int num[10][10], i, j, count = 0;

    for(i = 0; i < 10; i++){
        for(j = 0; j <= i; j++){
            num[i][j] = count;
            count++;
            printf("%d\t", num[i][j]);
        }
        printf("\n");
    }
}