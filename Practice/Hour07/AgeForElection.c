//find min and max peopel who vote
#include <stdio.h>
//Find max age or oldest peeple who vote
int findMax(int array[], int i, int size){
    int max = -1;
    for(i = 0; i < size; i++){
        if(array[i] > max) max = array[i];
    }
    return max;
}
//Find min age or youngest peeple who vote
int findMin(int array[], int i, int size){
    int min = 999;
    for(i = 0; i < size; i++){
        if(array[i] < min) min = array[i];
    }
    return min;
}
//Find average age
int findAverage(int array[], int i, int size){
    int sum = 0;
    int average;
    for(i = 0; i < size; i++){
        sum += array[i];
    }
    return average = sum / size;
}
//Driver code
int main(){
    //Declare variables
    int age[5];
    int minAge, maxAge, average;
    int i = 0;
    int size = sizeof(age)/sizeof(age[0]);
    //Input
    printf("Enter age: ");
    for(i = 0; i < size; i++){
        scanf("%d", &age[i]);
    }
    //Process
    minAge = findMin(age, i, size);
    maxAge = findMax(age, i, size);
    average = findAverage(age, i, size);
    printf("The oldest people is %d years old.\nThe youngest people is %d years old.\nAverage age is %d years old.\n", maxAge, minAge, average);
}