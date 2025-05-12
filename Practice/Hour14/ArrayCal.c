#include <stdio.h>
//sum
int sum(int *first, int *second){
    int sum;
    sum = *first + *second;
    return sum;
}
//Driver code
int main(){
    //Decalre array size variable
    int size;
    //Input array size
    printf("Array size : ");
    scanf("%d",&size);
    //Assign array size and Declare another variables
    int array[size];
    int length = sizeof(array)/sizeof(array[0]);
    int i, first, second;
    //Initialize elements of array by use sum function to assign in each index
    for(i = 0; i < length; i++){
        printf("Array at %d index : ", i+1);
        fflush(stdin);
        scanf("%d %d", &first, &second);
        array[i] = sum(&first, &second); 
    }
    //Output array sign index
    printf("Array index : ");
    for(i = 0; i < length; i++){
        printf("%d ", i+1);
    }
    printf("\n");
    //Output value of each element in array
    printf("Value index : ");
    for(i = 0; i < length; i++){
        printf("%d ", array[i]);
    }
}