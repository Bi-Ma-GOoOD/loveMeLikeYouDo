#include <stdio.h>
// finc number and compare number which is greater than
long long int maxNumber(long long int max, long long int a){
    long long int cmp_1 = max + a;
    long long int cmp_2 = a;
    if(cmp_1 <= cmp_2){
        return cmp_2;
    }else{
        return cmp_1;
    }
}
// Driver Code
int main(){
    // Declare variables
    long long int input;
    long long int i;
    // Input
    // printf("Enter number: ");
    scanf("%lld",&input);
    // Initialize array
    long long int array[input];
    for(i = 0; i < input; i++){
        scanf("%lld", &array[i]);
    }
    // Calculate Max sub array
    long long int max = array[0];
    long long int temp = array[0];
    for(i = 1; i < input; i++){
        temp = maxNumber(temp, array[i]);
        if(max <= temp) max = temp;
    }
    printf("%lld", max);
}