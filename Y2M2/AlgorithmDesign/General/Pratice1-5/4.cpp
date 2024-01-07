#include <cstdio>
#include <algorithm>
// กำหนดค่า n ให้มีค่าเท่ากับ 7
# define N 6
using namespace std;

int main(){
    int array[N], array_check[N], i;
    // input
    for(i = 0; i < N; i++){
        // printf("Enter number : ");
        scanf("%d", &array[i]);
    }
    // initial array check
    for(i = 0; i < N; i++){
        array_check[i] = i+1;
    }
    // sort array
    sort(array, array + N);
    // compare array with array_check to find lost number
    for(i = 0; i < N; i++){
        // printf("array : %d\n", array[i]);
        // printf("check : %d\n", array_check[i]);
        if(array[i] != array_check[i])
            printf("Number %d doesn't exist in input.", array_check[i]);
    }
}