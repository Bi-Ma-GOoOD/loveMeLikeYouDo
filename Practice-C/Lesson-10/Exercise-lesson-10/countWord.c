#include <stdio.h>
#define MAX 100

int main(){
    // Declare variables
    char word[MAX];
    int space = 1, i;
    // UI
    printf("Enter word : ");
    gets(word);
    // Find space
    for(i = 0; *(word+i) != '\0'; i++){
        if(*(word+i) == ' ') space++;
    }
    // UI
    printf("\tYou Enter\n");
    printf("\t%s", word);
    printf("\nSentences have %d words\t %d spaces", space, space);
}