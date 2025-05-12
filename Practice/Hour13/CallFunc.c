#include <stdio.h>
//Function 2
void callMeTwo(){
    printf("Hello, there! I am Two\n");
}
//Function 1
void callMeOne(){
    printf("Hello, world! I am One\n");
    callMeTwo();
}

int main(){
    callMeOne();
    return 0;
}