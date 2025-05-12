#include <stdio.h>
#include <string.h>

int main(){
    char str1[10], str2[10], str3[30];
    strcpy(str1, "impress");
    printf("Str1 is %s\n", str1);
    printf("Str1 have %d characters\n\n",strlen(str1));

    strcpy(str2, "im");
    printf("Str2 is %s\n", str2);
    printf("Str2 have %d characters\n\n",strlen(str2));

    if(strcmp(str1, str2) == 0) printf("compare str1 and str2 with strcmp(); => str1 equal str2\n");
    else printf("Compare str1 and str2 with strcmp(); => str1 not equal str2\n");

    if(strncmp(str1, str2, 2) == 0) printf("Compare str1 and str2 with strncmp(); => str1 equal str2\n");
    else printf("Compare str1 and str2 wit strncmp(); => str1 not equal str2\n");

    strcpy(str3, str1);
    printf("\nConcatenate %s with %s, result is %s ", str1, str2, strcat(str3, str2));
}