#include <stdio.h>

int count_word(char s[]);

int main(){
    char word[10000];
    printf("Input your word: ");
    gets(word);
    printf("You have %d words.",count_word(word));
}

int count_word(char s[]){
    int count = 0;
    int i = 0;
    while(s[i] != '\0'){
        if(s[i] == ' ') {count++;}
        i++;
    }
    return count+1;
}