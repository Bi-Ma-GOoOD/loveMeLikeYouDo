#include <stdio.h>

int ft(int n, int sum){
    if(n <= 0) return 0;
    else ft(n-1, n + sum);
}

int main(){
    int ans = ft(5,0);
    printf("Sum: %d\n", ans);
}