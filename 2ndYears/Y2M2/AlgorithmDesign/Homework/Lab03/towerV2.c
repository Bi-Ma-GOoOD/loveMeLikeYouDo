// ทำไมส่งไม่ได้วะงง แม่งรันไม่ได้ ไอ้สัส
#include <stdio.h>
// find number in array
int binarySearch(int array[], int start, int end, int target){
    int mid;
    while(start <= end){
        mid = end + (end - start)/2;
        if(array[mid] > target){
            end = mid - 1;
        }else{
            start = mid + 1;
        }
    }
    return start;
}

// find amount tower function
int findTower(int array[], int n){
    int amountTower = 0;
    int temp_array[n];
    int i;
    for(i = 0; i < n; ++i){
        int checkNumber = binarySearch(temp_array, 0, amountTower - 1, array[i]);
        if(checkNumber < amountTower){
            temp_array[checkNumber] = array[i];
        }else{
            temp_array[amountTower++] = array[i];
        }
    }
    return amountTower;
}
int main(){
    // Define variables
    int input, i;
    int towers;
    // Input for create array
    // printf("Enter input: ");
    scanf("%d", &input);
    // Initial array size
    int arr[input];
    // Initial array values
    for(i = 0; i < input; i++){
        scanf("%d", &arr[i]);
    }
    // Call function
    towers = findTower(arr, input);
    // Output
    printf("%d", towers);
}