//Dynamic programming : Fibonacci - bottom up

#include <stdio.h>

int main(){
    // difine variable
    int input;
    // input
    printf("Fibo of : ");
    scanf("%d",&input);
    // initial array fibo
    int fibo[input+1];
    fibo[0] = 0;
    fibo[1] = 1;
    // calculate bottom up fino
    for(int i = 2; i <= input; i++){
        fibo[i] = fibo[i-2] + fibo[i-1];
    }
    // output
    printf("Fibo(%d) = %d\n", input, fibo[input]);
}