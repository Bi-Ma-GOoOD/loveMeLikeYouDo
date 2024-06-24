#include <stdio.h>

int main(){
    FILE *fptr;
    //Choose r mode to read from CreateFile.txt
    fptr = fopen("D:\\AB-BiMaGOoOD\\Tob-taun\\Practice\\Hour02\\easySlip.c", "r");
    //Create array for store the content form file
    char myString[100];
    //Read content and store inside myString
    //fgets can read only one line at a time

    //fgets(myString, 100, fptr);
    
    //if you want to read more than one line
    while(fgets(myString, 100, fptr)){
        printf("%s", myString);
    }
    //Print the file content
    printf("%s", myString);
    //Close file
    fclose(fptr);
}