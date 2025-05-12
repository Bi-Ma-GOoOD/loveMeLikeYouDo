#include <stdio.h>

int main(){
    int table[9][9], i, j, x;
    // ใส่ค่าให้กับตารางสูตรคูณ
    for(i = 1; i <= 9; i++){
        for(j = 1; j <= 9; j++){
            table[i-1][j-1] = i*j;
        }
    }
    
    printf("* |\t1\t2\t3\t4\t5\t6\t7\t8\t9\n");
    printf("- - - - - - - - - - - - - - - - - - - -");
    printf("- - - - - - - - - - - - - - - - - -\n");
    
    for(i = 0; i < 9; i++){
        printf("%d |\t", i+1);
        for(j = 0; j < 9; j++){
            printf("%d\t",table[i][j]);
        }
        printf("|\n");
    }
}