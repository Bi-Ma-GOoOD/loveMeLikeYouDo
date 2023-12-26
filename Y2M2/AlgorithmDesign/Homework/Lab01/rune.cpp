#include <cstdio>
#include <algorithm>
using namespace std;

int main(){
    int rune_amount, group, i;
    // Input
    scanf("%d %d",&rune_amount, &group);
    // Initialize array
    int runes[rune_amount];
    for(i = 0; i < rune_amount; i++){
        scanf("%d", &runes[i]);
    }
    // Sort
    sort(runes, runes+rune_amount);
    // Initial power between bob(min) and darth(max)
    int left = 0, right = rune_amount - 1;
    int bob = 0, darth = 0;
    while(left < group){
        bob += runes[left];
        darth += runes[right];
        left ++;
        right --;
    }
    // Calculate different power
    int result = darth - bob;
    printf("%d",result);
}