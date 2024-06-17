#include <stdio.h>

int main(){
    // Declare variables
    const int maxScore = 500;
    int userScore;
    // Input
    printf("Enter user score: ");
    scanf("%d",&userScore);
    //Calculate
    float percentage = ((float)userScore/maxScore)* 100.0;
    //Output
    printf("User's percentage is %.2f\n", percentage);
    
}