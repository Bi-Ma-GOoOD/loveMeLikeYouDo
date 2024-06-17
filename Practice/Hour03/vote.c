#include <stdio.h>
#include <stdbool.h>

int main(){
    //Declare variables
    int votingAge = 18;
    int voter;
    //Input
    printf("Please enter your age for voting : ");
    scanf("%d",&voter);
    //Check age
    int check = voter >= votingAge;
    //Election
    if(check){
        printf("\tCongratulations you can use your rights to vote.\nThanks for use your voice!!!\n^.^");
    }else{
        printf("\tSorry, your age cannot use for voting.\nBut we're thank you for interesting in election.");
    }
}