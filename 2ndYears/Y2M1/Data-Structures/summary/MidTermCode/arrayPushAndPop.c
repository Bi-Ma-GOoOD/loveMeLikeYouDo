#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

#define MAX 10;
int stackdata[10];
int top = -1;

int push(int what){
    if(top < 10-1){
        top++;
        stackdata[top] = what;
        return 1;
    }
    return -1;
}

int pop(){
    int r;

    if(top > -1){
        r = stackdata[top];
        stackdata[top] = 0;
        top--;
        return r;
    }
    return -1;
}

int main(){
    push(7);
    push(12);
    printf("Pop 1 = %d\n", pop());
    printf("Pop 2 = %d\n", pop());
}