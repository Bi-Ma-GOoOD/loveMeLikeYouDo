#include <stdio.h>

int main(){
    //Declare variables
    int vote[4] = {20, 46, 19, 92};
    int *ptr = vote;
    int i;
    //Output
    for(i = 0; i < 4; i++){
        printf("%p : %d\n", ptr+i, *(ptr+i));
    }
}