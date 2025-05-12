#include <cstdio>
using namespace std;

int main(){
    int array_num[9] = {8, 7, 9, 2, 3, 1, 5, 4, 6};
    int i, j;
    int min, temp;
    // output unsort array
    printf("Before Sort\n");
    for(i = 0; i < 9; i++){
        printf("%d ", array_num[i]);
    }
    // selection sort
    for(i = 0; i < 9; i++){
        min = i;
        for(j = i+1; j < 9; j++){
            if(array_num[min] > array_num[j]){
                min = j;
            }
        }
        temp = array_num[i];
        array_num[i] = array_num[min];
        array_num[min] = temp;
    }
    // output sorted array
    printf("\nAfter Sort\n");
    for(i = 0; i < 9; i++){
        printf("%d ", array_num[i]);
    }
}