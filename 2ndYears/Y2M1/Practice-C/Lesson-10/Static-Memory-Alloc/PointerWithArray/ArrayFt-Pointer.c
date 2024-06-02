#include <stdio.h>

int main(){
    char data[9] = "Computer", data2[9] = "Keyboard";
    char *p = data;

    printf("Now, First element of data variable inside at address %p\n", &data[0]);
    printf("Now, First element of data2 variable inside at address %p\n", &data2[0]);
    printf("\nAssign p = data;\n");
    printf("Pointer p point to data variable at address %p\n", p);
    printf("and pointer p point to '%c' character\n", *p);

    p = data2;

    printf("\nAfter change pointer p point to data2 variable ( assign p = data2; )\n");
    printf("Pointer p point to data2 variaable at address %p\n", p);
    printf("and pointer p point to '%c' character\n", *p);
}