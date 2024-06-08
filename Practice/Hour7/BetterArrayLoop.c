#include <stdio.h>

int main(){
    //Declare variables
    int evenNumber[5] = {2, 4, 6, 8, 10};
    //Array size
    int size = sizeof(evenNumber)/sizeof(evenNumber[0]);
    //Output
    printf("size of even number use %d bytes\n",sizeof(evenNumber));
    printf("array name evenNumber have %d elements\n", size);
    for(int i = 0; i < size; i++){
        printf("%d\n", evenNumber[i]);
    }
}