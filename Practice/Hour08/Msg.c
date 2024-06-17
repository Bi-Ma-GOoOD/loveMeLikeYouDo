#include <stdio.h>

int main(){
    //Declare variables
    char sentence[256];
    char reciever[16];
    char senter[16];
    int i, size;
    //Input
    printf("From : ");
    scanf("%s", senter);
    printf("To : ");
    scanf("%s", reciever);
    //We use fgets to read string from stdin
    printf("Enter : ");
    fflush(stdin);
    fgets(sentence, sizeof(sentence), stdin);
    printf("- - - - - - - FORMAT - - - - - - -\n\n");
    //Output
    printf("From : %s\nTo : %s\n\n\t%s", senter, reciever, sentence);
}