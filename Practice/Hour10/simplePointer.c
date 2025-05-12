#include <stdio.h>

int main(){
    //Declare variables
    int myAge = 20;
    int *pointer = &myAge;
    //Ouput
    printf("Note :\n\t1. When used in declaration (int* ptr), it creates a pointer variable.\n\t2. When not used in declaration, it act as a dereference operator.\n");
    printf("Variable Value\t\t[myAge] : %d\n", myAge);
    printf("Variable Address\t[&myAge] : %p\n", &myAge);
    printf("Pointer Value\t\t[pointer] : %p\n", pointer);
    printf("Pointer point to value\t[*pointer] : %d\n", *pointer);
}