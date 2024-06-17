//Love
#include <stdio.h>

int main(){
    //Declare variables
    char buff[256];
    int i = 0;
    //Input
    printf("Enter you alphabet->mose: ");
    scanf("%s", buff);
    //Process
    for(i; buff[i] != '\0'; i++){
        if(buff[i] == 'L' || buff[i] == 'l'){
            printf("xo\nxo\nxo");
        }else if(buff[i] == 'O' || buff[i] == 'o'){
            printf("\n\n");
            printf("xo\nox\nxo");
        }else if(buff[i] == 'V' || buff[i] == 'v'){
            printf("\n\n");
            printf("xo\nxo\nxx");
        }
    }
}