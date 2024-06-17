//I want to make 2D - Arrays show character Z
#include <stdio.h>

int main(){
    //Declare variables
    int array[5][5];
    int i, j;
    int body = 2, width = 2;
    //Lets make Z
    for(i = 0; i < 4; i++){
        for(j = 0; j < 5; j++){
            if(j % 2 != 0){
                printf(".");
            }else{
                printf("^");
            }
        }
        printf("\n");
    }
}