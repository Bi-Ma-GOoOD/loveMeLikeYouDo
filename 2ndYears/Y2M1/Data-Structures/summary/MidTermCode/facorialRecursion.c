#include <stdio.h>

int factorial(int n){
    if(n == 1) return n;
    else return n *factorial(n-1);
}

int main(){
    int ans = factorial(5);
    printf("Sum: %d\n", ans);
}