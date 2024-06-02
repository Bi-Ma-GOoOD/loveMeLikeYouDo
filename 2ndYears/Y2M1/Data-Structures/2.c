#include <stdio.h>
#include <string.h>

typedef struct{
    char student_name[100];
    int student_point;
}Student;

int main(){
    Student std[5];
    char tmp_name[100];// tmp as for Temporary Name
    float avg; // avg as for Average
    float total = 0.0;

    for(int i = 0;i < 5; i++) {
        printf("Enter Student Name: ");
        scanf("%s", tmp_name);
        strcpy(std[i].student_name,tmp_name);
        printf("Enter Student Point: ");
        scanf("%d", &std[i].student_point);
        total = total + std[i].student_point;
    }
    avg = total / 5;
    printf("Average Point: %.2f\n", avg);
    printf("Student who has more than average point is\n");
    for(int i = 0; i < 5 ; i++){
        if(std[i].student_point >= avg) {printf("Student Name: %s || Score: %d\n", std[i].student_name,std[i].student_point);}
        continue;
    }
}