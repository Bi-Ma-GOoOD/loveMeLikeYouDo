#include <stdio.h>

char catn_str(char a1[], char b1[]);
int main(){
    char a[] = "Hello_";
    char b[] = "World!";
    printf("Before concatenate\n");
    printf("A = %s B = %s", a, b);
    printf("\n---------------\n");
    printf("After Concatenate\n");
    catn_str(a, b);
}

char catn_str(char a1[], char b1[]){
    int i = 0;
    int j = 0;

    while(a1[i] != '\0'){
        i++;
    }
    while(b1[j] != '\0'){
        a1[i] = b1[j];
        i++;
        j++;
    }
    a1[i] = '\0';
    printf("%s",a1);
}