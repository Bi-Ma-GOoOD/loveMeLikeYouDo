#include <stdio.h>

int main(){
    // Declare variables
    int student[6], subject[6];
    int i, j, num1, num2, num3, num4, num5, sum = 0, all = 0;
    // UI Midterm
    printf("Midterm test score\n");
    printf("Please input Test1-Test5 scores e.g. 8 7 10 5 9\n");
    // Input Midterm-score in each student
    for(i = 0; i < 5; i++){
        printf("Student %d score : ", i+1);
        scanf("%d %d %d %d %d", &subject[0], &subject[1], &subject[2], &subject[3], &subject[4], &subject[5]);
        // Take sum Midterm-score to each student
        for(j = 0; j < 5; j++){
            if(subject[j] > 10){
                printf("Each test score not over 10\n");
                printf("Student %d score : ", i+1);
                scanf("%d %d %d %d %d", &subject[0], &subject[1], &subject[2], &subject[3], &subject[4], &subject[5]);
                sum += subject[j];
                student[i] = sum;
                // Test value add operation score
                // printf("%d\n", student[i]);
            }else{
                sum += subject[j];
                student[i] = sum;
                // Test value add operation score
                // printf("%d\n", student[i]);
            }
        }
        sum = 0;
        // Test value midterm-score
        // printf("student %d midterm-score : %d\n",i+1, student[i]);
    }
    // UI Final
    printf("\n\nFinal test score\n");
    printf("Please input Test1-Test5 scores e.g. 8 7 10 5 9\n");
    // Input final-score in each student
    for(i = 0; i < 5; i++){
        // Test value midterm score for each student
        // printf("Student %d midterm-score : %d\n", i+1, student[i]);
        printf("Student %d score : ", i+1);
        scanf("%d %d %d %d %d", &subject[0], &subject[1], &subject[2], &subject[3], &subject[4], &subject[5]);
        // Take sum final-score to each student
        for(j = 0; j < 5; j++){
            if(subject[j] > 10){
                printf("Each test score not over 10\n");
                printf("Student %d score : ", i+1);
                scanf("%d %d %d %d %d", &subject[0], &subject[1], &subject[2], &subject[3], &subject[4], &subject[5]);
                all += subject[j];
                student[i] += all;
                // Test value add operation score
                // printf("%d\n", student[i]);
                all = 0;
            }else{
                all += subject[j];
                student[i] += all;
                // Test value add operation score
                // printf("%d\n", student[i]);
                all = 0;
            }
        }
        // Test value final score
        // printf("student %d final-score : %d\n",i+1, student[i]);
    }
    // UI
    printf("\n\nTotal test score\n");
    printf("Student 1 score : %d\n", student[0]);
    printf("Student 2 score : %d\n", student[1]);
    printf("Student 3 score : %d\n", student[2]);
    printf("Student 4 score : %d\n", student[3]);
    printf("Student 5 score : %d\n", student[4]);
}