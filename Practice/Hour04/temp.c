#include <stdio.h>

int main(){
    char buf[2];

    scanf("%c", buf);
    if(buf[0] == 'y'){
        printf("yes\n");
    }else{
        printf("I don't know.TT");
    }
}