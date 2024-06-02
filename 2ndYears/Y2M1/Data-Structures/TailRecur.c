#include <stdio.h>

int ft(int n , int sum); // Tail Recursion
int fr(int n); // Linear Recursion

int main(){
    int number = 5;
    int all = 2;
    printf("The result of\nTail Recursion is: %d\nLinear Recursion is: %d\n",ft(number,all), fr(number));
}

int ft(int n, int sum){
    if(n <= 0) return sum;
    else return ft(n-1, n+sum);
}

int fr(int n){
    if(n <= 0) return 0;
    else return ft(n-1, n);
}