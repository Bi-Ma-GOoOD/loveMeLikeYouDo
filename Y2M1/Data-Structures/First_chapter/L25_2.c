#include <stdio.h>

int main(){
    char s1[100] = "Hello_";
    char s2[100] = "Student!";
    int i = 0, j = 0;
    
    printf("Before Concatenate\n");
    printf("S1 = %s S2 = %s",s1, s2);

    while(s1[i] != '\0'){
        i++;
    }
    while(s2[j] != '\0'){
        s1[i] = s2[j];
        i++;
        j++; 
    }
    s1[i] = '\0';
    printf("\n--------------------\n");
    printf("After Concatenate\n");
    printf("S1 = %s S2 = %s",s1, s2);
}