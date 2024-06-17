#include <stdio.h>
#include <string.h>

int i;

int main(){
    //Declare variables
    char check[64] = "123Tue";
    char passwords[64], name[16];
    //Input
    printf("Enter name : ");
    scanf("%s", name);
    for(i = 0; i < 4; i++){
        printf("Enter password : ");
        scanf("%s", passwords);
        if(strcmp(passwords, check) == 0){
            printf("Welcome back! %s\n", name);
            break;
        }else if(i < 3){
            printf("Try again...\n");
        }
    }
    if(i == 4) printf("Sorry \"%s\" your account locked for 10 seconds...", name);
}