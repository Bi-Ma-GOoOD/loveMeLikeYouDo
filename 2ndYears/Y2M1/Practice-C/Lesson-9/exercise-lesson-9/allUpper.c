#include <ctype.h>
#include <stdio.h>
#include <string.h>
#define MAX_CHAR 80

int main(){
    // Declare variables
    char text[MAX_CHAR];
    int i;
    //UI
    printf("Enter text to uppercase ( Ex. apple -> APPLE): ");
    fgets(text, MAX_CHAR, stdin);
    //Change lower -> upper case
    for(i = 0; i < strlen(text) && (int)text[i] != 10; i++){
        printf("%d \n", (int)text[i]);
        if(((int)text[i] >= 65 && (int)text[i] <= 90) || (((int)text[i] >= 97 && (int)text[i] <= 122))){
            text[i] = toupper(text[i]);
        }else{
            printf("You must enter letters only. Good luck!");
            return 0;
        }
    }
    //UI
    printf("%s", text);
}