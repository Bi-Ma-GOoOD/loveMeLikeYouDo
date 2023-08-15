#include <stdio.h>
#include <string.h>

int main(){
    struct student{
        char *name;
        int age;
        char *nickname;
    };
    struct student s;
    struct student *sPtr;

    // strcpy(s.name, "Somsak");
    s.name = "Somsak";
    s.age = 19;
    s.nickname = "Poleon";
    sPtr = &s;
    printf("%s\n", s.name);
    printf("%s\n", s.nickname);
    printf("%d\n", sPtr->age);
    return 0;
}