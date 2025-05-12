#include <cstdio>
// กำหนดให้ ค่า n = 5
#define N 5
using namespace std;

int main(){
    int array_input[N];
    int mid;
    int i = 0;
    // กำหนดใ้ห i มีค่าเท่ากับ 4
    int j = 4;
    // input
    for(i = 0; i < N; i++)
        scanf("%d", &array_input[i]);
    // find i
    mid = N/2;
    if(array_input[mid] < j)
        for(i = mid; i < N; i++){
            if(array_input[i] == j){
                printf("Found");
            }
        }
    else if(array_input[mid] > j)
        for(i = mid; i >= 0; i--){
            if(array_input[i] == j){
                printf("Found");
            }
        }
}