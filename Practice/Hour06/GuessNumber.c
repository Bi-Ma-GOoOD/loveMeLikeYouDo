#include <stdio.h>

int i;

int main(){
    //Declare variables
    int input_number;
    int guess_number = 99;
    char type[64];
    int hint = 0;
    //Input
    printf("This is guess number game.\nYou can type /help for more information or type /play for quick play.\n");
    scanf("%s", type);
    if((type[0] == '/') && (type[1] == 'H' || type[1] == 'h')){
        printf("\tHints is already for even round only.\nAnd you can use 3 times(Warning : Use conciously ^.^).\n");
        printf("Are you ready to play?\n");
        printf("type\n\tY(es)\n\tN(o)\n");
        fflush(stdin);
        scanf("%s", type);
        if(type[0] == 'Y' || type[0] == 'y'){
            for(i = 0; i < 10; i++){
                printf("\tEnter the number(Round %d/%d) : ", i+1, 10);
                scanf("%d", &input_number);
                if((input_number == guess_number) && (i+1 <= 10)){
                    printf("Congratulations you use %d time(s) to guess and it correct.\n", i+1);
                    break;
                }else if(input_number != guess_number){
                    if(i+1 == 10){
                        printf("Sorry you use all 10 times to guess TT, and the answer is %d\n", guess_number);
                    }else{
                        printf("%d is not the correct number.\n", input_number);
                        if(hint < 3){
                            printf("Y(es) for hints or N(o) for deny hints.\n");
                            printf("Type Y or N only : ");
                            printf("-> ");
                            fflush(stdin);
                            scanf("%s", type);
                            if(type[0] == 'Y' || type[0] == 'y'){
                                hint++;
                                if((i+1)% 2 == 0){
                                    if(input_number < guess_number){
                                        printf("Hint : Try more than number\n");
                                    }else{
                                        printf("Hint : Try less than number\n");
                                    }
                                }else{
                                    printf("Sorry I can't give you now TT\n");
                                }
                                printf("You have %d more hint(s) left.\n", 3-hint);
                            }else if(type[0] == 'N' || type[0] == 'n'){
                                printf("You are brave XD.\n");
                                continue;
                            }
                        }else if(hint == 3){
                            printf("Hints isn't available.\n");
                        }
                    }
                }
            }
        }else if(type[0] == 'N' || type[0] == 'n'){
            printf("See you next time ^.^\n");
        }else{
            printf("%s is not my command sorry TT.\n", type);
        }
    }else if((type[0] == '/') && (type[1] == 'P' || type[1] == 'p')){
        for(i = 0; i < 10; i++){
            printf("\tEnter the number(Round %d/%d) : ", i+1, 10);
            scanf("%d", &input_number);
            if((input_number == guess_number) && (i+1 <= 10)){
                printf("Congratulations you use %d time(s) to guess and it correct.\n", i+1);
                break;
            }else if(input_number != guess_number){
                if(i+1 == 10){
                    printf("Sorry you use all 10 times to guess TT, and the answer is %d\n", guess_number);
                }else{
                    printf("%d is not the correct number.\n", input_number);
                    if(hint < 3){
                        printf("Y(es) for hints or N(o) for deny hints.\n");
                        printf("Type Y or N only : ");
                        printf("-> ");
                        fflush(stdin);
                        scanf("%s", type);
                        if(type[0] == 'Y' || type[0] == 'y'){
                            hint++;
                            if((i+1)% 2 == 0){
                                if(input_number < guess_number){
                                    printf("Hint : Try more than number\n");
                                }else{
                                    printf("Hint : Try less than number\n");
                                }
                            }else{
                                printf("Sorry I can't give you now TT\n");
                            }
                            printf("You have %d more hint(s) left.\n", 3-hint);
                        }else if(type[0] == 'N' || type[0] == 'n'){
                            printf("You are brave XD.\n");
                            continue;
                        }
                    }else if(hint == 3){
                        printf("Hints isn't available.\n");
                    }
                }
            }
        }
    }else{
        printf("%s is not my command sorry TT.\n", type);
    }
}