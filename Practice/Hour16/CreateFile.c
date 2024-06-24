#include <stdio.h>

int main(){
    FILE *fptr;
    //Open file with absolute path in writing mode
    fptr = fopen("C:\\users\\User\\Desktop\\CreateFile.txt", "a");
    //Write some text to the file
    fprintf(fptr, "\nBiMaGOoOD : Hiiii Toooo!!!!\n[From 08:35 Mon 24/06/2024]");
    //Close file
    fclose(fptr);
}