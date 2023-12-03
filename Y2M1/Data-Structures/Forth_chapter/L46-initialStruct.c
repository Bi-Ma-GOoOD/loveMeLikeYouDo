#include <stdio.h>

struct income{
    float salary, bonus;
    int age;
};

int main(){
    struct income somsri;
    somsri.salary = 18000.00;
    somsri.bonus = 30000.00;
    somsri.age =  23;
    printf("%f\n",somsri.salary);
    printf("%f\n",somsri.bonus);
    printf("%f\n",somsri.age);
    return 0;
}