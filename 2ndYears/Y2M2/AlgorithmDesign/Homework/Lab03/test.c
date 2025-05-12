#include <stdio.h>

int binarySearch(int tower_tops[], int low, int high, int key) {
    while (low <= high) {
      printf("- - - - - -\nlow: %d\n", low);
      printf("high: %d\n", high);
        int mid = low + (high - low) / 2;
        printf("mid : %d\n", mid);
        printf("key : %d\n", key);
        if (tower_tops[mid] > key) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    printf("Last low %d\n", low);
    return low;
}

int towers(int n, int k[]) {
    int towers = 0;  // Number of towers needed (start with 0)
    int tower_tops[n];  // Array to store the top box size of each tower

    for (int i = 0; i < n; ++i) {
        int index = binarySearch(tower_tops, 0, towers - 1, k[i]);
        printf("index: %d\n", index);
        printf("towers before plus: %d\n", towers);

        if (index < towers) {
            tower_tops[index] = k[i];  // Update the top box size of the tower
        } else {
            tower_tops[towers++] = k[i];  // Initialize the top box size of the new tower
            printf("towers after plus: %d\n", towers);
        }
    }

    return towers;
}

int main() {
    int n;
    scanf("%d", &n);

    int k[n];
    for (int i = 0; i < n; ++i) {
        scanf("%d", &k[i]);
    }

    int min_towers = towers(n, k);
    printf("Ans: %d\n", min_towers);

    return 0;
}