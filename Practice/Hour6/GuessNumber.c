#include <stdio.h>

int main(){
    //Declare variables
    int input_number;
    int guess_number = 67;
    char type[64];
    int i;
    //Input
    printf("This is guess number game.\nYou can type /help for more information or type /play for quick play.\n");
    scanf("%s", type);
    if((type[0] == '/') && (type[1] == 'H' || type[1] == 'h')){
        printf("You can type /h for hints ^.^\n");
        printf("Are you ready to play?\n");
        printf("type\n\tY(es)\n\tN(o)\n");
        fflush(stdin);
        scanf("%s", type);
        if(type[0] == 'Y' || type[0] == 'y'){
            for(i = 0; i < 10; i++){
                printf("Enter the number : ");
                scanf("%d", &input_number);
                if(input_number == guess_number){
                    printf("Congratulations you use %d time(s) to guess and it correct.\n", i+1);
                    break;
                }else if(input_number != guess_number){
                    printf("%d is not the correct number.\n", input_number);
                    printf("Y(es) for hints or N(o) for deny hints.\n");
                    printf("Type Y or N only : ");
                    printf("-> ");
                    fflush(stdin);
                    scanf("%s", type);
                    if(type[0] == 'Y' || type[0] == 'y'){
                        if(input_number < guess_number){
                            printf("Hint : Try more than number\n");
                        }else{
                            printf("Hint : Try less than number\n");
                        }
                    }else if(type[0] == 'N' || type[0] == 'n'){
                        printf("You are brave XD.\n");
                        continue;
                    }
                }
            }
        }else if(type[0] == 'N' || type[0] == 'n'){
            printf("See you next time ^.^\n");
        }else{
            printf("%s is not my command sorry TT.\n");
        }
    }else if((type[0] == '/') && (type[1] == 'P' || type[1] == 'p')){
        for(i = 0; i < 10; i++){
            printf("Enter the number : ");
            scanf("%d", &input_number);
            if(input_number == guess_number){
                printf("Congratulations you use %d time(s) to guess and it correct.\n", i+1);
                break;
            }else if(input_number != guess_number){
                printf("%d is not the correct number.\n", input_number);
                printf("Y(es) for hints or N(o) for deny hints.\n");
                printf("Type Y or N only : ");
                printf("-> ");
                fflush(stdin);
                scanf("%s", type);
                if(type[0] == 'Y' || type[0] == 'y'){
                    if(input_number < guess_number){
                        printf("Hint : Try more than number\n");
                    }else{
                        printf("Hint : Try less than number\n");
                    }
                }else if(type[0] == 'N' || type[0] == 'n'){
                    printf("You are brave XD.\n");
                    continue;
                }
            }
        }
    }else{
        for(i = 0; type[i] != '\0'; i++){
            printf("%s", type[i]);
        }
        printf(" is not in my command sorry TT.\n", type);
    }
}