// Mamximum subSequence sum

#include <stdio.h>
// this function make to compare number which one is greater than and return it
int sum(int cmp1, int cmp2){
    cmp1 = cmp1 + cmp2;
    if(cmp1 < cmp2) return cmp2;
    else return cmp1;
}
// driver code
int main(){
    // define variables
    int input, i;
    printf("Input number : ");
    scanf("%d",&input);
    // intial array
    int array[input];
    for(i = 0; i < input; i++){
        scanf("%d",&array[i]);
    }
    // calculate
    int temp;
    int cmp = array[0];
    for(i = 1; i < input; i++){
        temp = sum(cmp,array[i]);
        cmp = temp;
    }
    // output 
    printf("Mamximum Sub Sequence sum = %d\n", cmp);
}