#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

void checkMeow(char stringA[], int number);

int main(){
    int loop, numString, i;

    // printf("Input Round: ");
    scanf("%d",&loop);

    for(i = 0; i < loop; ++i){
        // printf("Input number of strings: ");
        scanf("%d",&numString);
        numString += 2;

        char word[numString];
        // printf("Input String: ");
        scanf("%s",word);
        checkMeow(word, numString);
    }
}

void checkMeow(char stringA[], int number){
    char *ptr = stringA;
    char answer[number];
    char previous = '\0';
    int i;
    int j = 0;

    for(i = 0; i < number && stringA[i] != '\0' ; ++i){
        stringA[i] = tolower(stringA[i]);
    }

    for(i = 0; i < number; ++i){
        if(ptr[i] == previous){
            continue;
        }else{
            answer[j] = ptr[i];
            previous = answer[j];
            j++;
        }
    }
    // printf("%s\n",answer);
    if(strcmp("meow", answer)) {printf("NO\n");}
    else {printf("YES\n");}
}