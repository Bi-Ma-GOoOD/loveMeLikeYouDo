#include <stdio.h>

int factorial(int a);

int main(){
    int n = 5;
    printf("%d! is: %d",n,factorial(n));

}
    int factorial(int n){
        if(n == 1) return 1;
        else return n*factorial(n-1);
    }