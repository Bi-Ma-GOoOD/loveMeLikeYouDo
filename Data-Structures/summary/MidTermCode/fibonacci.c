#include <stdio.h>

int fibonacci(int n){
    if(n == 1) return n;
    else if(n == 2) return 1;
    else  return fibonacci(n-1) + fibonacci(n-2);
}

int  main(){
    int ans =  fibonacci(5);
    printf("Result: %d\n", ans);
}