#include <stdio.h>
#include <string.h>

int main(){
    //Declare array
    char target_word[128];
    char sentence[128];
    //Input target word
    printf("Enter target word : ");
    fflush(stdin);
    scanf("%s", target_word);
    //Initialize variables
    int length_target = strlen(target_word);
    int first_pos, i = 0, t = 0;
    int j = length_target;
    //Input sentence
    printf("Enter sentence : ");
    fflush(stdin);
    fgets(sentence, sizeof(sentence), stdin);
    // printf("Target length : %d\n", length_target);
    //Process
    while(sentence[i] != '\0'){
        if(sentence[i] == target_word[t]){
            // printf("Sentence pos[%d]: %c\n", i, sentence[i]);
            // printf("Target_word pos[%d]: %c\n", t, target_word[t]);
            j--;
            t++;
            // printf("j : %d\n", j);
            // printf("t : %d\n", t);
        }else if(j == 0){
            break;
        }else{
            // printf("j : %d\n", j);
            j = length_target;
            t = 0;
        }
        i++;
    }
    // printf("i = %d\n", i+1);
    if(j == 0) printf("Found \"%s\" at position %d in the sentence.\n", target_word, ((i+1)-length_target));
    else printf("Not found \"%s\" in the sentence.\n", target_word);
}