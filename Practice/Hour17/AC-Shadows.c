#include <stdio.h>
//turn to percent function
int percent();
int main(){
    //Declare variable
    FILE *file;
    char date[16];
    float balance;
    int week;
    //Assign variable to read mode and create file if this file name is does not exist before.
    // file = fopen("D:\\AB-BiMaGOoOD\\Lyrics\\AC-Shadows.txt", "w");
    //But now we have this file and we want to append file 
    file = fopen("D:\\AB-BiMaGOoOD\\Lyrics\\AC-Shadows.txt", "w");
    //Input for create a templete
    printf("Enter week #");
    scanf("%d", &week);
    printf("Enter date : ");
    fflush(stdin);
    fgets(date, 100, stdin);
    printf("Enter balance of the week : ");
    scanf("%f", &balance);
    printf("Week #%d\nDate : %sBalance of this week : %.2f\n", week, date, balance);
    // fprintf(file, "Week #%d\nDate : %sBalance of this week : %.2f\n", week, date, balance);
    //Finished for writing file
    //Now we will read number from file
    file = fopen("C:\\Users\\User\\Desktop\\CreateFile.txt", "r");
    while(fscanf(file, "%f", &balance) == 1){
        printf("Balance : %.2f\n", balance);
    }
    fclose(file);
    printf("Done.\n");
}