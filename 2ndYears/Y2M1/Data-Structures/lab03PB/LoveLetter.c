#include <stdio.h>
#include <stdlib.h>

int main(){
    char word[128];
    char check_word[128];
    int *ptr_i, i, j;
    ptr_i = &i;
    char *ptr_checkword = check_word;

    fgets(word,128,stdin);

    for(i = 0; word[i] != '\0'; i++){
        if(word[i] == 'a' && word[i+1] == 'p' && word[i+2] == word[i]){
            *ptr_checkword = 'a';
            ptr_checkword++;
            *ptr_i += 2;
        }
        else if(word[i] == 'e' && word[i+1] == 'p' && word[i+2] == word[i]){
            *ptr_checkword = 'e';
            ptr_checkword++;
            *ptr_i += 2;
        }
        else if(word[i] == 'i' && word[i+1] == 'p' && word[i+2] == word[i]){
            *ptr_checkword = 'i';
            ptr_checkword++;
            *ptr_i += 2;
        }
        else if(word[i] == 'o' && word[i+1] == 'p' && word[i+2] == word[i]){
            *ptr_checkword = 'o';
            ptr_checkword++;
            *ptr_i += 2;
        }
        else if(word[i] == 'u' && word[i+1] == 'p' && word[i+2] == word[i]){
            *ptr_checkword = 'u';
            ptr_checkword++;
            *ptr_i += 2;
        }else{
            *ptr_checkword = word[i];
            ptr_checkword++;
        }
    }
    *ptr_checkword = '\0';
    printf("%s",check_word);
}