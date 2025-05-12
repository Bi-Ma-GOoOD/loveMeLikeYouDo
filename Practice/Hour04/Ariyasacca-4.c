//The Four Noble Truths of Sufferings
#include <stdio.h>
#include <unistd.h>

int main(){
    //Declare variables
    char buff[256], name[16], choice[4], choice_2[4];
    //Input
    printf("Ariyasacca : Hello my name is Ariyasacca.\n");
    sleep(2);
    printf("Ariyasacca : What is your name?\n");
    printf("-> ");
    scanf("%s", name);
    // sleep(2);
    printf("Ariyasacca : Hi %s.How can I help you?\n", name);
    printf("You can input : \n\tY(yes) : for know about Ariyasacca.\n\tN(no) : for cancle chat with Ariyasacca.\n\tP(pass) : for quick talk with Ariyasacca.\nfor more information about me ^.^\n");
    printf("%s : ", name);
    scanf("%s", choice);
    //Process
    if(choice[0] == 'Y' || choice[0] == 'y'){
        printf("\tMy full name is Ariyasacca 4. My creator built me for help you to get out of any depression anxiety or everything that make you feel uncomfortable.\n");
        printf("By I have 4 questions for you and you should answer all of it OK? ^.^\n");
        printf("Let's start\n\t1. What is your suffering?\n\t2. What is the cause of suffering?\n\t3. What is your result if you get out of your suffering?\n\t4. What is the path to make get out of suffering and happy ^.^\n");
        printf("This is information about me.Are you ready to try? :D\n-> Y(es) or N(o)\n");
        printf("%s : ", name);
        scanf("%s", choice_2);
        if(choice_2[0] == 'Y' || choice_2[0] == 'y'){
            printf("Ariyasacca : What is your suffering? %s?\n", name);
            printf("%s : ", name);
            fflush(stdin);
            scanf("%s", buff);
            sleep(2);
            printf("Ariyasacca : And, what is the cause of suffering?\n");
            printf("%s : ", name);
            fflush(stdin);
            scanf("%s", buff);
            sleep(2);
            printf("Ariyasacca : Then, What is your result if you get out of your suffering?\n");
            printf("%s : ", name);
            fflush(stdin);
            scanf("%s", buff);
            sleep(2);
            printf("Ariyasacca : Finally, What is the path to make get out of suffering and happy ^.^\n");
            printf("%s : ", name);
            fflush(stdin);
            scanf("%s", buff);
            sleep(2);
            printf("Ariyasacca : Feel better ????\n");
            printf("%s : ", name);
            fflush(stdin);
            scanf("%s", buff);
            printf("Ariyasacca : Hahaha. I hope you enjoy and happay all day. Thank you to talk with me goodbyeeee.\n");
            printf("%s : ", name);
            fflush(stdin);
            scanf("%s", buff);
        }else if(choice_2[0] == 'N' || choice_2[0] == 'n'){
            printf("Ariyasacca : I hope you enjoy and happay all day good byeeeee ^.^");

        }else{
            printf("Ariyasacca : I don't understand this command TT. You can call me later.");
        }
    }else if(choice[0] == 'N' || choice[0] == 'n'){
        printf("Ariyasacca : I'm so sadddddddd TT.");
    }else if(choice[0] == 'P' || choice[0] == 'p'){
        printf("Ariyasacca : I so happy to talk you ^.^\n");
        printf("Ariyasacca : What is your suffering? %s?\n", name);
        printf("%s : ", name);
        fflush(stdin);
        scanf("%s", buff);
        sleep(2);
        printf("Ariyasacca : And, what is the cause of suffering?\n");
        printf("%s : ", name);
        fflush(stdin);
        scanf("%s", buff);
        sleep(2);
        printf("Ariyasacca : Then, What is your result if you get out of your suffering?\n");
        printf("%s : ", name);
        fflush(stdin);
        scanf("%s", buff);
        sleep(2);
        printf("Ariyasacca : Finally, What is the path to make get out of suffering and happy ^.^\n");
        printf("%s : ", name);
        fflush(stdin);
        scanf("%s", buff);
        sleep(2);
        printf("Ariyasacca : Feel better ????\n");
        printf("%s : ", name);
        fflush(stdin);
        scanf("%s", buff);
        printf("Ariyasacca : Hahaha. I hope you enjoy and happay all day. Thank you to talk with me goodbyeeee.\n");
        printf("%s : ", name);
        fflush(stdin);
        scanf("%s", buff);
    }else{
        printf("Ariyasacca : I don't understand this command TT. You can call me later. TT");
    }
}