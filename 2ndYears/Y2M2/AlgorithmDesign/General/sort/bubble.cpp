#include <cstdio>
using namespace std;

int main(){
    int num[9] = {8, 7, 9, 2, 3, 1, 5, 4, 6};
    int temp, pointer, i, j;
    // output unsort array
    printf("Before Sort\n");
    for(i = 0; i < 9; i++){
        printf("%d ", num[i]);
    }
    // bubble sort
    for(i = 0; i < 9; i++){
        for(j = 0; j < 9 - i; j++){
            if(num[j] > num[j+1]){
                temp = num[j];
                num[j] = num[j+1];
                num[j+1] = temp;
            }
        }
    }
    // output sorted array
    printf("\nAfter Sort\n");
    for(i = 0; i < 9; i++){
        printf("%d ", num[i]);
    }
}