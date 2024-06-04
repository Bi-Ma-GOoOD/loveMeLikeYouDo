#include <stdio.h>

int main(){
    //Declare variables
    char can[4], can_2[4];
    int i;
    //Input
    printf("- Do you have problem in Life?\n");
    printf("Answer : ");
    scanf("%s", can);
    //Decision
    if(can[0] == 'Y' || can[0] == 'y'){
        printf("- Can you do something about it?\n");
        printf("Answer : ");
        scanf("%s", can_2);
        //Decision
        printf("Then why worry, keep going!\t^.^\n");
    }else{
        printf("Then why worry, keep going!\t^.^\n");
    }
}