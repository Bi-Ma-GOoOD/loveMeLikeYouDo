#include <stdio.h>
#include <unistd.h>

int main(){
    int i = 3;
    while(i > 0){
        sleep(2);
        printf("%d\n", i);
        i--;
    }
    sleep(1);
    printf("Happy New Year!\n");
}