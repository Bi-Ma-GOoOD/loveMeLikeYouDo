#include <cstdio>
// กำหนดให้ n = 4
# define N 4
using namespace std;
// find min funcion
int findMin(int oldNumber, int newNumber){
    int leastNumber = oldNumber;
    if(newNumber < 0)
        newNumber = newNumber * -1;
    if(newNumber < oldNumber)
        leastNumber = newNumber;
    return leastNumber;
}

int main(){
    int min, temp, i, j, newValue;
    int oldNumber = 99999;
    int matrix[N][N];
    // input initial array
    for(i = 0; i < N; i++){
        for(j = 0; j < N; j++){
            scanf("%d", &matrix[i][j]);
        }
    }
    // calculate min
    for(i = 0; i < N; i++){
        for(j = 0; j < N; j++){
            if( matrix[i][j+1] != '\0')
                temp = matrix[i][j] - matrix[i][j+1];
                newValue = findMin(oldNumber, temp);
                oldNumber = newValue;
        }
    }
    // output
    printf("\nAnswer : %d", oldNumber);
}