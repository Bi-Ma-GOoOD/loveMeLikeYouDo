#include <stdio.h>
#include <string.h>

int main(){
    char greeting[5][50] = {"Good Morning",
                            "Good Afternoon",
                            "Good Evening",
                            "Good Night",
                            "Good idiot you don't know how many hour per day ?"};
    char time[6];
    int i, j;

    printf("Please insert time in format xx.xx\n");
    printf("e.g. 07.00, 15.30, 24.00 etc. \n");
    printf("What time is it? : ");
    fgets(time, 6, stdin);

    while(time[2] != '.'){
        printf("Your time are wrong format, please try again.\n");
        printf("What time is it? : ");
        fgets(time, 6, stdin);
    }

    if(strcmp(time, "12.00") < 0) i = 0;
    else if(strcmp(time, "17.00") < 0) i = 1;
    else if(strcmp(time, "21.00") < 0) i = 2;
    else if(strcmp(time, "24.00") < 0) i = 3;
    else i = 4;

    for(j = 0; j < strlen(greeting[i]); j++){
        printf("%c", greeting[i][j]);
    }
}
