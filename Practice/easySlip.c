#include <stdio.h>

int main(){
    // Declare variables
    int items = 10;
    float cost_per_item = 13.25;
    float total_cost = cost_per_item * items;
    char unit = 36;
    //Output
    printf("Number of items: %d\n", items);
    printf("Cost per item: %.2f %c\n", cost_per_item, unit);
    printf("Total cost = %.2f %c\n", total_cost, unit);
    return 0;
}