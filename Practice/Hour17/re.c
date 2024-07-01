#include <stdio.h>

int main(){
    FILE *file;
    char Mystring[100];
    file = fopen("D:\\AB-BiMaGOoOD\\Lyrics\\PowerIsPower.txt", "r");
    //Read file
    while(fgets(Mystring, 100, file) != NULL){
        printf("%s", Mystring);
    }
    fclose(file);
}