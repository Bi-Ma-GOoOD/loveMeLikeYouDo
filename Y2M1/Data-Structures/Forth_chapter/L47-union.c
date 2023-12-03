#include <stdio.h>
#include <string.h>

union profile{
    char name[20];
    int age;
    char grade;
}var1;

int main(){
    printf("Size fo var1 = %d\n", sizeof(var1));
    strcpy(var1.name, "Somsri");
    var1.age = 10;
    var1.grade = 'A';

    printf("Name = %s\n",var1.name);
    printf("Age = %d\n", var1.age);
    printf("Grade = %d\n", var1.grade);
    return 0;
}
