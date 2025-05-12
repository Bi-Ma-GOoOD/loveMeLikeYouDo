#include <stdio.h>
#include <string.h>

struct Student{
    char name[100];
    int point;
}student[5];

int main(){
    float sum = 0;
    float average;

    for(int i = 0; i < 5 ; i++){
        printf("Enter your name: ");
        scanf("%s", student[i].name);
        printf("Enter your score: ");
        scanf("%d", &student[i].point);
        sum += student[i].point;
    }

    for(int j = 0; j < 5; j++){
        if(student[j].point > (sum/5)) printf("Name: %s\n", student[j].name);
    }
}