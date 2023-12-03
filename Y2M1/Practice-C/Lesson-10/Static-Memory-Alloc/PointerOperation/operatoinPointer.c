#include <stdio.h>

int main(){
    char data[9] = "Computer";
    int num[3] = {1, 2, 3}, count;
    float avg[5] = {1.1, 2.2, 3.3, 4.4, 5.5};
    char *ch = data;
    int *i = num;
    float *f = &avg[3];

    printf("Pointer ch point to data variable at address %p\n", ch);
    printf("Pointer ch point to value : %c\n", *ch);
    printf("After assign ch = ch + 3; pointer ch point to address %p\n", ch+3);
    printf("Pointer ch point to value : %c\n\n", *(ch+3));

    for(count = 0; count < 3; count++){
        printf("address num[%d] = %p\n", count, &num[count]);
    }

    printf("Pointer i point to address %p\n", i);
    printf("After assign i = i+1; pointer i point to address %p\n", i+=1);
    printf("Now i point to num[1], so value is %d\n", *i);
    printf("After plus value of i with 1, value is %d\n", *i+1);
    printf("After minus value of i with 1, value is %d\n\n", (*i)-1);

    printf("Value of pointer f is %f\n", f[0]);
    printf("After forward poiner f 1 step, value is %f\n", *(f+1));
    printf("After backward pointer f 3 step, value is %f\n", f[-3]);
}