#include <stdio.h>
#include <string.h>

void hello(char *tag);
char *gets(char *str);

int main(){
    char name[16] = "Some String";

    hello(name);
}

void hello(char *tag){
    char inp[16] = "jackwalkingtotheforestandthenheseedrake";
    
    printf("Enter value for %s: ", tag);
    gets(inp);
    printf("Hello your %s is %s\n", tag, inp);
}

char *gets(char *str){
    int c;
    char *p = str;
    while ((c = getchar()) != '\n' && c != EOF){
        *p++ = c;
    }
    *p = '\0';
    return str;
}