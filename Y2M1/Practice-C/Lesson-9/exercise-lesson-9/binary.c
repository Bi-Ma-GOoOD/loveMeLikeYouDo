#include <stdio.h>

int main(){
    int bit[17], divide, binary, number, i;
    int index = 0;
    // UI
    printf("enter your number for change to binary format: ");
    scanf("%d", &number);
    // Binary Operators
    while(number > 0){
        binary = number % 2;
        number /= 2;
        bit[index] = binary;
        index++;
    }
    // UI
    for(i = 0; i < index; i++){
        printf("%d ", bit[i]);
    }
}