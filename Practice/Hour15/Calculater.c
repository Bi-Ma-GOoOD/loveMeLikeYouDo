#include <stdio.h>
#include <math.h>
//Declaration functions
float add(float arr[], int length);
float subtract(float first, float second);
float multiply(float arr[], int length);
float divide(float first, float second);
int fac(int number);
float powerNumber(float base, float power);
//Driver code
int main(){
    char choice;
    int size, i;
    float result, first, second;
    printf("This is calculator program\nYou can choose operation you want to do\n");
    printf("Choose A(add), S(subtract), M(multiply), D(divide), F(factorial), P(power)\n> > > ");
    fflush(stdin);
    scanf("%c",&choice);
    if(choice == 'A' || choice == 'a'){
        printf("Note! summation need at least 2 numbers.\nHow many number do you want to summation : ");
        scanf("%d", &size);
        float arr[size];
        int length = sizeof(arr)/sizeof(arr[0]);
        printf("Enter number : ");
        for(i = 0; i < length; i++){
            scanf("%f", &arr[i]);
        }
        result = add(arr, length);
        for(i = 0; i < length; i++){
            printf("%.3f", arr[i]);
            if(i == length - 1) printf(" =");
            else printf(" + ");
        }
        printf(" %.3f\n", result);
    }else if(choice == 'S' || choice == 's'){
        printf("Note! sustraction need at least 2 numbers.\n");
        printf("Enter first and second number : ");
        scanf("%f %f", &first, &second);
        result = subtract(first, second);
        printf("%.3f - %.3f = %.3f\n", first, second, result);
    }else if(choice == 'M' || choice == 'm'){
        printf("Note! Multiplication need at least 2 numbers.\nHow many number do you want to multiply : ");
        scanf("%d", &size);
        float arr[size];
        int length = sizeof(arr)/sizeof(arr[0]);
        printf("Enter number : ");
        for(i = 0; i < length; i++){
            scanf("%f", &arr[i]);
        }
        result = multiply(arr, length);
        for(i = 0; i < length; i++){
            printf("%.3f", arr[i]);
            if(i == length - 1) printf(" =");
            else printf(" x ");
        }
        printf(" %.3f\n", result);
    }else if(choice == 'D' || choice == 'd'){
        printf("Note! Division need at least 2 numbers.\n");
        printf("Enter first and second number : ");
        scanf("%f %f", &first, &second);
        result = divide(first, second);
        printf("%.3f divided by %.3f = %.3f\n", first, second, result);
    }else if(choice == 'F' || choice == 'f'){
        int number;
        printf("Enter number : ");
        scanf("%d", &number);
        result = fac(number);
        printf("Factorial of %d (", number);
        for(i = number; i > 0; i--){
            printf("%d", i);
            if(i == 1) printf(") =");
            else printf(" x ");
        }
        printf(" %d\n", (int)result);
    }else if(choice == 'P' || choice == 'p'){
        printf("Note! Power need at least 2 numbers.\n");
        printf("Enter base and power number : ");
        scanf("%f %f", &first, &second);
        result = powerNumber(first, second);
        printf("%.3f powered by %.3f = %.3f\n", first, second, result);
    }
}
float add(float arr[], int length){
    int i;
    float sum = 0.0;
    for(i = 0; i < length; i++){
        sum += arr[i];
    }
    return sum;
}
float subtract(float first, float second){
    return first - second;
}
float multiply(float arr[], int length){
    int i;
    float result = 1.0;
    for(i = 0; i < length; i++){
        result *= arr[i];
    }
    return result;
}
float divide(float first, float second){
    return first / second;
}
int fac(int number){
    if(number == 1){
        return 1;
    }else{
        return number * fac(number - 1);
    }
}
float powerNumber(float base, float power){
    return pow(base, power);
}