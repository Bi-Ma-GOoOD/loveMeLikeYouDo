#include <stdio.h>
#include <string.h>

int main(){
    char str[80], tmp;
    char *p = str;
    int i, j;

    printf("Enter word : ");
    fgets(str, 80, stdin);

    for(i = 0; i < strlen(str)-1; i++){
        for(j = i+1; j <= strlen(str)-1; j++){
            if(*(p+i) > *(p+j)){
                tmp = *(p+i);
                *(p+i) = *(p+j);
                *(p+j) = tmp;
            }
        }
    }
    printf("Your word ( sort by character ) is : %s\n", str);
}