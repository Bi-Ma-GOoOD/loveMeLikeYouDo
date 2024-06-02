#include <stdio.h>

void printSubset(int temp[], int bound, int i){
    int j;
    for(j = 0; j < i; j++){
        printf("%d ", temp[j]);
    }
    printf("\n");
}
void callSubset(int i, int set[], int size, int bound){
    int temp[size];
    for(i; i < bound; i++){
        temp[i] = set[i];
        printSubset(temp, bound, i+1);
    }
    callSubset(i, set, size, bound+1);
}
// driver code
int main(){
    // Define variables
    int i, arr_size, member;
    // Initialize array size
    scanf("%d", &arr_size);
    int set[arr_size];
    // Initialize member in set array
    for(i = 0; i < arr_size; i++){
        scanf("%d", &set[i]);
    }
    // Calculate all possible subsets
    for(i = 0; i < arr_size; i++){
        // printf("%d", set[i]);
        callSubset(i, set, arr_size, 2);
    }
}