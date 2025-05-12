#include <stdio.h>

int main(){
    FILE *fptr;
    //Create file name Power is Power
    fptr = fopen("D:\\AB-BiMaGOoOD\\Lyrics\\PowerIsPower.txt", "r");
    //Writer a file
    //fprintf(fptr, "Song Name : Power is Power\nSinger Name : SZA, The Weeknd, Travis Scott\nProducers : Myles Martin, Daleala, Ricky Reed & The Weeknd\nAlbum Name : Game of Thrones\n\n");
    /*Read a file
    1. Create a store content variable
    2. if-else if not exist*/
    //Store content variable
    char mySong[100];
    //Read file
    if(fptr != NULL){
        while(fgets(mySong, 100, fptr)){
            printf("%s", mySong);
        }
    }else{
        printf("This file is not exist.\n");
    }
    //Close file
    fclose(fptr);
}