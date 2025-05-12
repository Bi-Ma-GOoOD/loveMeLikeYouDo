#include <stdio.h>
#include <stdlib.h>

int compareInt(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int binarySearch(int arr[], int n, int target) {
    int left = 0, right = n - 1, result = -1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] <= target) {
            result = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return result + 1;
}

void calculateDamage(int arrayMonster[], int arrayWeapon[], int weapon, int monster);

int main() {
    int amountMonster, amountWeapon;
    int i, j;
    
    scanf("%d", &amountMonster);
    int monsterLife[amountMonster];
    for (i = 0; i < amountMonster; ++i) {
        scanf("%d", &monsterLife[i]);
    }
    
    scanf("%d", &amountWeapon);
    int damageWeapon[amountWeapon];
    for (j = 0; j < amountWeapon; ++j) {
        scanf("%d", &damageWeapon[j]);
    }
    
    qsort(monsterLife, amountMonster, sizeof(int), compareInt);
    
    calculateDamage(monsterLife, damageWeapon, amountWeapon, amountMonster);
}

void calculateDamage(int arrayMonster[], int arrayWeapon[], int weapon, int monster) {
    int i;
    
    for (i = 0; i < weapon; ++i) {
        int count = binarySearch(arrayMonster, monster, arrayWeapon[i]);
        printf("%d\n", count);
    }
}