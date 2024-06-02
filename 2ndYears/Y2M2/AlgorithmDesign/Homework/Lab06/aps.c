#include <stdio.h>

int printSubset(int a[], int amount){
    int i;
    for(i = 0; i < amount; i++){
        printf("%d ", a[i]);
    }
    return 0;
}
// driver code
int main(){
    // Define variables
    int i, j, arr_size, member;
    int index = 0;
    int amount = 0;
    // Initialize array size
    scanf("%d", &arr_size);
    int set[arr_size];
    // Initialize member in set array
    for(i = 0; i < arr_size; i++){
        scanf("%d", &set[i]);
    }
    // Calculate all possible subsets
    for(i = 0; i <= index; i++){
        int temp[amount];
        temp[i] = set[i];
        printSubset(temp, amount);
        if(index ++ <= arr_size){
            index++;
            amount++;
            i = 0;
        }else if(index ++ > arr_size){
            i ++;
        }
    }
}