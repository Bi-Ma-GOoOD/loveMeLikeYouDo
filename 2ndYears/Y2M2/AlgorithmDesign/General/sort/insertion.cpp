#include <cstdio>
using namespace std;

int main(){
    int num[9] = {9, 8, 7, 6, 5, 4, 3, 2, 1};
    int temp, pointer, i, j;
    // output unsort array
    printf("Before Insertion Sort\n");
    for(i = 0; i < 9; i++){
        printf("%d ", num[i]);
    }
    // insertion sort
    for(i = 1; i < 9; i++){
        temp = num[i];
        j = i - 1;
        while(j >= 0 && num[j] > temp){
            num[j+1] = num[j];
            j--;
        }
        num[j+1] = temp;
    }
    // output sorted array
    printf("\nAfter Insertion Sort\n");
    for(i = 0; i < 9; i++){
        printf("%d ", num[i]);
    }
}