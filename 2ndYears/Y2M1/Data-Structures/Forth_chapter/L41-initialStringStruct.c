#include <stdio.h>
#include <string.h>

struct letter{
    char name[20];
    char address[30];
    char message[40];
};

int main(){
    struct letter first;
    printf("Enter name: ");
    scanf("%s",first.name);
    printf("Enter address: ");
    scanf("%s",first.address);
    strcpy(first.message, "How r u?");

    printf("\nName is %s",first.name);
    printf("\nAddress is %s",first.address);
    printf("\nMessage is %s",first.message);
    return 0;
}