#include <stdio.h>

int main(){
    // Declare variables
    int raft_per_car, cross_time, amount_car;
    // Input
    printf("Enter raft per car & cross river time & amount car : ");
    scanf("%d %d %d", &raft_per_car, &cross_time, &amount_car);
    // Calculate least raft
    int least_raft = (amount_car/raft_per_car)+1;
    // Input car destination time
    int destinate_time[amount_car];
    int i;
    for(i = 0; i < amount_car; i++)
        scanf("%d", &destinate_time[i]);
    // Find least time
    int arr_size = sizeof(destinate_time)/sizeof(destinate_time[0]);
    int least_time = destinate_time[arr_size-1] + cross_time;
    // Output
    printf("Cross the river at least time : %d\n", least_time);
    printf("Use the least raft : %d", least_raft);
}