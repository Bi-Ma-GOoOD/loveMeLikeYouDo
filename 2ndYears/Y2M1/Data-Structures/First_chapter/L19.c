#include <stdio.h>

int main(){
    char sentence[100];
    int count = 1, c = 0;
    printf("Enter sentence: ");
    gets(sentence);
    while(sentence[c] != '\0'){
        if(sentence[c] == ' ') count++;
        c++;
    }
    printf("number of words: %d\n", count);
    return 0;
}