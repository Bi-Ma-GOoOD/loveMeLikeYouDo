#include <stdio.h>
#include <string.h>

int main(){
    struct profile{
        char name[20];
        int age;
        char grade;
    }student[10];

    strcpy(student[0].name, "Manee");
    student[2].age = 12;
    student[4].grade =  'A';
    printf("%s\n", student[0].name);
    printf("%d\n", student[2].age);
    printf("%c\n", student[4].grade);
}