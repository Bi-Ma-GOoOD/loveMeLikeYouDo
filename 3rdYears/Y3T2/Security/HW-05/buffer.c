#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *gets(char *str);

int main(){
    char str1[8];
    char str2[8];
    int valid = 0;

    gets(str1);
    gets(str2);
    if(strncmp(str1, str2, 8) == 0)
        valid = 1;
    printf("Buffer 1: str1(%s), str2(%s), valid(%d)\n", str1, str2, valid);
    printf("@valid = %p, @str1 = %p, @str2 = %p", &valid, &str1, &str2);
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