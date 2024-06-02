// ข้อที่ 1.1
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
// Merges two subarrays of arr[].
void merge(int arr[], int l, int m, int r)
{
	int i, j, k;
	int n1 = m - l + 1;
	int n2 = r - m;
	// Create temp arrays
	int L[n1], R[n2];
	// Copy data to temp arrays L[] and R[]
	for (i = 0; i < n1; i++)
		L[i] = arr[l + i];
	for (j = 0; j < n2; j++)
		R[j] = arr[m + 1 + j];
	// Merge the temp arrays back into arr[l..r]
	i = 0;
	j = 0;
	k = l;
	while (i < n1 && j < n2) {
		if (L[i] <= R[j]) {
			arr[k] = L[i];
			i++;
		}
		else {
			arr[k] = R[j];
			j++;
		}
		k++;
	}
	// Copy the remaining elements of L[],
	while (i < n1) {
		arr[k] = L[i];
		i++;
		k++;
	}

	// Copy the remaining elements of R[],
	while (j < n2) {
		arr[k] = R[j];
		j++;
		k++;
	}
}
// sub-array of arr to be sorted
void mergeSort(int arr[], int l, int r)
{
	if (l < r) {
		int m = l + (r - l) / 2;

		// Sort first and second halves
		mergeSort(arr, l, m);
		mergeSort(arr, m + 1, r);

		merge(arr, l, m, r);
	}
}
// Global Variables for mutex room
bool empty = true;
int j;
void enter_room(int arr[], int size){
    int j = 0; 
    for(j = 0; j < size; j++){
        while(empty == false); // Busy waiting for room
        room_activate(arr, j);
    }
}
int room_activate(int arr[], int j){
    empty = false;
    printf("[False]\t\t\tActivity %d\tuse room %d hours.\n", j+1, arr[j]);
    leave_room(j);
    return 0;
}
int leave_room(int j){
    printf("[True]\t\t\tActivity %d\tuse room finished.\n", j+1);
    printf("\n");
    empty = true;
    return 0;
}

// Driver code
int main(){
    // Declare variables
    int activity;
    // Input activity
    printf("Activity amount: ");
    scanf("%d", &activity);
    // Declare array size
    int start[activity], finish[activity];
    int arr_size = sizeof(start)/ sizeof(start[0]);
    // Input value to array start
    int i;
    printf("Start :\n");
    for(i = 0; i < activity; i++){
        scanf("%d", &start[i]);
    }
    // Input value to array finish
    printf("Finish :\n");
    for(i = 0; i < activity; i++){
        scanf("%d", &finish[i]);
    }
    // Calculate time per activity
    for(i = 0; i < activity; i++){
        start[i] = finish[i] - start[i];
    }
    // Call merge sort for sorted activity
    mergeSort(start, 0, arr_size-1);
    // for(i = 0; i < arr_size; i++)
    //     printf("%d ", start[i]);
    printf("Status Room Empty\tActivity Use\ttime to use\n");
    enter_room(start, arr_size);
}