#include <stdio.h>

// compare function
int max(int cmp1, int cmp2){
    if(cmp1 > cmp2) return cmp1;
}
// driver code
int main(){
    int size;
    printf("Enter size: ");
    scanf("%d",&size);
    // initialize array
    int array[size];
    int i;
    for(i = 0; i < size; i++){
        scanf("%d",&array[i]);
    }
    // create new array but same size and initialize new array = 1
    int temp[size];
    for(i = 0; i < size; i++) temp[i] = 1; 
    // calculate long increasing subsequence
    int j;
    for(j = 1; j < size; j++){
        for(i = 0; i < j; i++ ){
            if(array[i] < array[j]){
                temp[j] = max(temp[i] + 1, temp[j]);
            }
        }
    }
    // find max value
    int max_value = temp[0];
    for(i = 1; i < size; i++){
        if(temp[i] > max_value) max_value = temp[i];
    }
    // output
    printf("Longest increasing subsequence: %d\n", max_value);
}