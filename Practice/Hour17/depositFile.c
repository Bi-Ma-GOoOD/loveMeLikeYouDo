#include <stdio.h>
//turn to percent functions
int percent();
int main(){
    //Declare variables
    FILE *file;
    char mode;
    char mainfile[] = "D:\\AB-BiMaGOoOD\\Lyrics\\AC-Shadows.txt";
    char minorFile[] = "C:\\Users\\User\\Desktop\\amountMoney.txt";
    int choice;
    char read[100];
    char date[16];
    float balance;
    int week;
    float sum = 0.00;
    float total = 2000.00;
    //Input for choose file
    printf("Notice : if you write content in AC-shadows.txt, your content will auto write the same content in amountMoney.txt too.\n");
    printf("Choose file to operate :\n\t1 - AC-Shadows.txt\n\t2 - amountMoney.txt\n");
    scanf("%d", &choice);
    if(choice == 1){
        //Input for choose mode
        printf("Mode for operate file have :\n\tr - Read content from file.\n\tw - Overwrite content to file.\n\ta - write append content to file.\n\td - Done close program.\n");
        printf("Enter mode to operate file : ");
        fflush(stdin);
        scanf("%c", &mode);
        if(mode == 'R' || mode == 'r'){
            file = fopen(mainfile, "r");
            if(file == NULL){
                printf("Can't open this file.\n");
            }else{
                //Read file
                while(fgets(read, 100, file) != NULL){
                    printf("%s", read);
                }
                fclose(file);
            }
        }else if(mode == 'W' || mode == 'w'){
            file = fopen(mainfile, "w");
            if(file == NULL){
                printf("Can't open this file.\n");
            }else{
                //Input for create a templete
                printf("Enter Week #");
                scanf("%d", &week);
                printf("Enter Date : ");
                scanf("%s", date);
                printf("Enter amount : ");
                scanf("%f", &balance);
                //Show output
                printf("Week #%d\nDate : %s\nBalance of this week : %.2f\n", week, date, balance);
                //Save content to the file
                fprintf(file, "Week #%d\nDate : %s\nBalance of this week : %.2f\n", week, date, balance);
                fclose(file);
                file = fopen(minorFile, "w");
                fprintf(file, "%.2f\n", balance);
                fclose(file);
            }
        }else if(mode == 'A' || mode == 'a'){
            file = fopen(mainfile, "a");
            if(file == NULL){
                printf("Can't open this file.\n");
            }else{
                //Input for create a templete
                printf("Enter Week #");
                scanf("%d", &week);
                printf("Enter Date : ");
                scanf("%s", date);
                printf("Enter amount : ");
                scanf("%f", &balance);
                //Show output
                printf("Week #%d\nDate : %s\nBalance of this week : %.2f\n", week, date, balance);
                //Save content to the file
                fprintf(file, "Week #%d\nDate : %s\nBalance of this week : %.2f\n", week, date, balance);
                fclose(file);
                file = fopen(minorFile, "a");
                fprintf(file, "%.2f\n", balance);
                fclose(file);
            }
        }else{
            printf("Done.\n");
        }
    }else if(choice == 2){
        //Input for choose mode
        printf("Mode for operate file have :\n\tr - Read content from file(Recommend).\n\tw - Overwrite content to file.\n\ta - write append content to file.\n\td - Done close program.\n");
        printf("Enter mode to operate file : ");
        fflush(stdin);
        scanf("%c", &mode);
        if(mode == 'R' || mode == 'r'){
            file = fopen(minorFile, "r");
            if(file == NULL){
                printf("Can't open this file.\n");
            }else{
                //Read file
                 while(fscanf(file, "%f", &balance) == 1){
                    sum += balance;
                }
                printf("Now you have %.2f Bath. And you need %.2f Bath to purchase Assassin Creed : Shadows\n", sum, total - sum);
                printf("%.2f %c / 100.00 %c \n", (sum/total)*100, 37, 37);
                fclose(file);
            }
        }else if(mode == 'W' || mode == 'w'){
            file = fopen(minorFile, "w");
            if(file == NULL){
                printf("Can't open this file.\n");
            }else{
                //Input balance of the week
                printf("Enter amount : ");
                scanf("%f", &balance);
                //Show output
                printf("Balance of this week : %.2f\n", balance);
                //Save content to the file
                fprintf(file, "%.2f\n", balance);
                fclose(file);
            }
        }else if(mode == 'A' || mode == 'a'){
            file = fopen(minorFile, "a");
            if(file == NULL){
                printf("Can't open this file.\n");
            }else{
                //Input for create a templete
                printf("Enter amount : ");
                scanf("%f", &balance);
                //Show output
                printf("%.2f\n", balance);
                //Save content to the file
                fprintf(file, "%.2f\n", balance);
                fclose(file);
            }
    }else{
        printf("Done.\n");
    }
    }
}