#include <stdio.h>
#include <string.h>
#define MAX_VALUE 100
int main(){
    char word[MAX_VALUE];

    printf("Enter word: ");
    fgets(word, MAX_VALUE, stdin);
    printf("Reverse of your word is \n");
    
    for(int i = strlen(word)-1; i >= 0; i--) printf("%c", word[i]);
}