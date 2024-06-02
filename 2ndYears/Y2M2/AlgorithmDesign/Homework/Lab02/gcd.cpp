#include <cstdio>
using namespace std;
// chnage integer to sumdigits
int sumDigits(int number){
    int sum = 0;
    while(number > 0){
        sum += number % 10;
        number /= 10;
    }
    return sum;
}
// Greate common divide
int gcd(int number1, int number2){
    int temp;
    int ans_function = number1;
    if(number2 == 1) return 0;
    while(number2 != 0){
        temp = number1 % number2;
        number1 = number2;
        number2 = temp;
        if(temp == 1){
            break;
        }
    }
    if(temp != 1) return ans_function;
    return 0;
}
// main function
int main(){
    int last, first, i;
    // input
    // printf("Enter gcd(last, first): ");
    scanf("%d %d", &last, &first);
    // find number in range that gcd != 1
    int answer[first-last] = {0}, j = 0;
    int digit;
    for(i = last; i <= first; i++){
        digit = sumDigits(i);
        // printf("last : %d\n", i);
        // printf("Digit: %d\n", digit);
        // printf("gcd (%d, %d)\n", i, digit);
        answer[j] = gcd(i, digit);
        // printf("Answer : %d\n", answer[j]);
        j++;
    }
    // print
    for(i = 0; i < j; i++){
        if(answer[i] != 0){
            printf("%d ", answer[i]);
        }
    }
}