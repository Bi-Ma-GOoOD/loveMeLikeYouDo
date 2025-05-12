#include <stdio.h>

int main(){
    //Declare start variables
    int size, i;
    //Input for assign array size
    printf("Input the number of elements to store in the array : ");
    scanf("%d",&size);
    //Declare array size
    int array[size];
    int length = sizeof(array)/sizeof(array[0]);
    //Initialize array
    for(i = 0; i < length; i++){
        printf("Element - %d : ", i);
        scanf("%d",&array[i]);
    }
    //Output
    int *ptr = array;
    printf("The elements you entered are :\n");
    for(i = 0; i < length; i++){
        printf("element - %d : %d\n", i, *(ptr+i));
    }
}