#include <stdio.h>

int count_str(char s[]);

int main(){
    char word[] = "cs231 Data Structure";
    int count_str(char s[]);
    printf("Length: %d \n",count_str(word));
}

int count_str(char s[]){
    int count = 0; 
    int i = 0;
    while(s[i] != '\0'){
        count++;
        i++;
    }
    return count;
}