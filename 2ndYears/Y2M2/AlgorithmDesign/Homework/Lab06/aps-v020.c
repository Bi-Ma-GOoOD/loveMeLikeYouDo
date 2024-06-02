#include <stdio.h>

//  PrintSubset function
void printSubsets(int arr[], int start, int end, int subset[], int index) {
    // Print current subset
    if (index != 0) {
        printf("%d", subset[0]);
        for (int i = 1; i < index; i++) {
            printf(" %d", subset[i]);
        }
        printf("\n");
    }

    // Generate subsets for elements starting from start
    for (int i = start; i <= end; i++) {
        // Add current element arr[i] to the subset
        subset[index] = arr[i];

        // printf("value i + 1 = %d\n", i + 1);
        // printf("value end = %d\n", end);
        // printf("value index + 1 = %d\n", index + 1);

        // Recur for remaining elements in arr[i+1..n-1]
        printSubsets(arr, i + 1, end, subset, index + 1);
    }
}
// Driver Code
int main() {
    // Define variable
    int n;
    // Input N
    scanf("%d", &n);
    // Initial array
    int arr[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    // Calculate subset
    int subset[n];
    printf("-\n");
    printSubsets(arr, 0, n - 1, subset, 0);

    return 0;
}