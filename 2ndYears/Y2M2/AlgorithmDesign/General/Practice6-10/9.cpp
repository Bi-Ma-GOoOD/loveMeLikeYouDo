#include <cstdio>
#include <algorithm>
// กำหนดค่า n = 5
#define N 4
using namespace std;

int main(){
    int array_input[N];
    int i;
    int sum = 0, j = 1;
    // input
    for(i = 0; i < N; i++){
        scanf("%d", &array_input[i]);
    }
    // sort input by merge sort
    sort(array_input, array_input+N);
    // calculate satisfaction
    for(i = 0; i < N; i++){
        if(array_input[i] < -1){
            sum += 0;
            // j++;
        }else{
            sum += array_input[i] * j;
            j++;
        }
    }
    // outout
    printf("%d", sum);
}