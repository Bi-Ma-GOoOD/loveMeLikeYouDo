#include <stdio.h>

int main(){
    // Declare variable
    int input;
    printf("Enter array size: ");
    scanf("%d",&input);
    // Initialize array size
    int arr[input];
    int i;
    for(i = 0; i < input; i++) scanf("%d",&arr[i]);
    // Declare variables for calculate Longest Increasing Subsequence
    int arr_size = sizeof(arr)/sizeof(arr[0]);
    int max = arr[0];
    // printf("Max = %d\n",max);
    for(i = 1; i < arr_size; i++){
        if(arr[i] > max){
            max = arr[i];
            // printf("Max in condition = %d\n",max);
            arr[i] = arr[i];
            // printf("arr[i] = %d\n",arr[i]);
        }else{
            arr[i] = 0;
        }
    }
    // Output
    for(i = 0; i < arr_size; i++){
        if(arr[i] != 0) printf("%d ", arr[i]);
    }
}