#include <stdio.h>

int Ack(int m, int n);

int main(){
    int a = 1,b = 1;
    printf("The result of Ackermann() is: %d\n",Ack(a,b));
}

int Ack(int m, int n){
    if(m == 0) return n+1;
    else if( m > 0 && n == 0) return Ack(m-1, 1);
    else if( m > 0 && n > 0) return Ack(m-1, Ack(m, n-1));
}