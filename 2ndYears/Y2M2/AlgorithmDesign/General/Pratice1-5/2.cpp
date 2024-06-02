#include <cstdio>
// กำหนดให้ ค่า n มีค่าเท่ากับ 8
# define N 8
using namespace std;

int main(){
    int number_stock[N];
    int number[N];
    int pos_positive = 0, pos_negative = 0;
    int i;
    // input
    for(i = 0; i < N; i++){
        // printf("Enter number : ");
        scanf("%d",&number[i]);
        if(number[i] > 0){
            pos_positive += 1;
        }else{
            pos_negative += 1;
        }
    }
    // insert positin negative and positive
    pos_negative = 0;
    for(i = 0; i < N; i++){
        if(number[i] < 0){
            number_stock[pos_negative] = number[i];
            pos_negative += 1;
        }else{
            number_stock[pos_positive] = number[i];
            pos_positive += 1;
        }
    }
    // output
    printf("[ ");
    for(i = 0; i < N; i++){
        printf("%d ", number_stock[i]);
    }
    printf("]");
}