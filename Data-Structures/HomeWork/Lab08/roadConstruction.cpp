#include <iostream>
using namespace std;

int  main(){
    int city, road, city1, city2, needMoreRoad;

    // printf("Enter city and Road: ");
    scanf("%d %d", &city, &road);

    for(int i = 0; i < road; ++i){
        // printf("enter edge road city to city: ");
        scanf("%d %d",&city1, &city2);
    }
    needMoreRoad = road -1;
    if(needMoreRoad < 0 ) printf("0", needMoreRoad);
    else printf("%d", needMoreRoad);
}