#include <stdio.h>
#include <stdbool.h>

int main(){
    //Declare variables
    bool myNameIsTrue = true;
    bool myNameIsFalse = false;
    bool meTrue = true;
    //Output
    printf("%d\n", myNameIsTrue);
    printf("%d\n", myNameIsFalse);
    printf("%d\n", meTrue == myNameIsTrue);
}