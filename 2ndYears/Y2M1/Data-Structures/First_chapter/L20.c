#include <stdio.h>

int main(){
    int matrix[3][3],row,col;
    for(int row = 0; row < 3; row++){
        for(int col = 0; col < 3; col++){
            printf("Enter numbers[%d] [%d]: ", row, col);
            scanf("%d",&matrix[row][col]);
        }
    }
    printf("Matrix\n");
    for(int row = 0; row < 3; row++){
        for(int col = 0; col < 3; col++){
            printf("%5d",matrix[row][col]);
        }
        printf("\n");
    }
}