#include <stdio.h>
//average element's array
void averageElement(int **sum, int **length, int **average){
    **average = **sum / **length;
}
//sum element's array
void sumElement(int array[5], int *length, int *sum, int *average){
    int i;
    for(i = 0; i < *length; i++){
        *sum += array[i];
    }
    averageElement(&sum, &length, &average);
}
int main(){
    //Declare variables
    int size, i;
    //Input array size
    printf("Enter array size : ");
    scanf("%d",&size);
    //Assign array size
    int array[size];
    int length = sizeof(array)/sizeof(array[0]);
    int sum, average;
    //Initialize array elements
    for(i = 0; i < length; i++){
        scanf("%d",&array[i]);
    }
    //Process
    sumElement(array, &length, &sum, &average);
    // averageElement(&length, &average, &sum);
    printf("Sum of array is : %d\nand average is : %d\n", sum, average);
}