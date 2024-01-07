// ขออนุญาตอาจารย์สร้างโค๊ดที่บังคับให้ใส่ตัวเลขแค่ 1 -5 นะคับ แต่จะใส่กี่ตัวเลขอันนี้ใส่ได้ถึง n จำนวนครับ
#include <cstdio>
#include <algorithm>
// กำหนดให้ค่า n = 9
# define N 9
using namespace std;

int main(){
    // array[0] คือตัวแทนของหมายเลข 1 
    int array[5] = {0};
    int number_stock[N];
    int i;
    // input number to number_stock
    for(i = 0; i < N; i++){
        // printf("Input number: ");
        scanf("%d", &number_stock[i]);
    }
    // assign frequency
    int frequency = N/2;
    // check same variable amount
    for(i = 0; i < N; i++){
        if(number_stock[i] == 1){
            array[0] += 1;
        }else if(number_stock[i] == 2){
            array[1] += 1;
        }else if(number_stock[i] == 3){
            array[2] += 1;
        }else if(number_stock[i] == 4){
            array[3] += 1;
        }else if(number_stock[i] == 5){
            array[4] += 1;
        }
    }
    // find variable that more than frequency
    for(i = 0; i < 5; i++){
        if(array[i] > frequency){
            printf("Answer is number %d have %d\n", i+1, array[i]);
        }
    }
}