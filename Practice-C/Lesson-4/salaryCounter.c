#include <stdio.h>
#include <math.h>

int main(){
    int emp_counter = 0; // Employee counter
    int high_sal_counter = 0;
    int medium_sal_counter = 0;
    int low_sal_counter = 0;
    int emp_amount;
    int salary;

    printf("How many employees do you have: ");
    scanf("%d", &emp_amount);

    while(emp_counter < emp_amount){
        printf("Enter employee salary: ");
        scanf("%d", &salary);
        if(salary >= 30000){
            high_sal_counter += 1;
            printf(" %d employees have %d bath.\n", emp_counter, salary);
        }
        else if(salary >= 20000){
            medium_sal_counter += 1;
            printf(" %d employees have %d bath.\n", emp_counter, salary);
        }
        else{
            low_sal_counter += 1;
            printf(" %d employees have %d bath.\n", emp_counter, salary);
        }
        emp_counter ++;
    }
    printf("High salary have %d employees.\n", high_sal_counter);
    printf("Medium salary have %d employees.\n", medium_sal_counter);
    printf("Low salary have %d employees.\n", low_sal_counter);
}