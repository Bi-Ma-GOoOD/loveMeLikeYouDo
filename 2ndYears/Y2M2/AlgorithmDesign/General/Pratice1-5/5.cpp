#include <cstdio>
// กำหนดตัวแปร n = 3
# define N 3
using namespace std;

int main(){
    int array[N][N], i, j, target;
    // input array
    for(i = 0; i < N; i++){
        for(j = 0; j < N; j++){
            scanf("%d", &array[i][j]);
        }
    }
    // input target number
    printf("Enter target number: ");
    scanf("%d", &target);
    // find number target in array
    for(i = 0; i < N; i++){
        for(j = 0; j < N; j++){
            if(target == array[i][j])
                printf("Number %d have in metrix.\nat column %d row %d", array[i][j], j+1, i+1);
        }
    }
}