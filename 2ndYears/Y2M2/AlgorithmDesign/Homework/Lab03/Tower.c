#include <stdio.h>

// find number in array
int binarySearch(int temp_array[], int first, int last, int target) {
    while (first <= last) {
        int mid = first + (last - first) / 2;
        if (temp_array[mid] > target) {
            last = mid - 1;
        } else {
            first = mid + 1;
        }
    }
    return first;
}
// find amount tower function
int findTower(int n, int arr[]) {
    int amountTower = 0;  
    int temp_array[n];  

    for (int i = 0; i < n; ++i) {
        int checkNumber = binarySearch(temp_array, 0, amountTower - 1, arr[i]);

        if (checkNumber < amountTower) {
            temp_array[checkNumber] = arr[i];  
        } else {
            temp_array[amountTower++] = arr[i];  
        }
    }
    return amountTower;
}

int main() {
    // Define variable
    int input;
    // Input for create array
    scanf("%d", &input);
    // Initial array size
    int number[input];
    // Initial array values
    for (int i = 0; i < input; ++i) {
        scanf("%d", &number[i]);
    }
    // Call function
    int towers = findTower(input, number);
    // Output
    printf("%d\n", towers);
}