// Sorry I have a boyfriend
#include <stdio.h>
// use to wait in time
#include <unistd.h>


int main(){
    printf("Nobody : Hello, world\n");
    sleep(2);
    for(int i = 0; i < 3; i++){
        printf(". ");
        sleep(1);
    }
    printf("\n");
    printf("World : Sry , I've boyfriend ^.^");
    return 0;
}