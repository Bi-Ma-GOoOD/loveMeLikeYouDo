#include <cstdio>
#include <algorithm>
using namespace std;

int main(){
    int people, max_weight, i, x, y, temp;
    int count = 0;
    // insert value
    scanf("%d %d", &people, &max_weight);
    // create array and initialize
    int duck[people];
    for(i = 0; i < people; i++ ){
        scanf("%d", &duck[i]);
    }
    // sort
    sort(duck, duck+people);
    // calculate duck
    int left = 0, right = people - 1;
    while(left <= right){
        if(duck[left] + duck[right] > max_weight){
            count ++;
            right --;
        }
        else{
            left ++;
            right --;
            count ++;
        }
    }
    // result
    printf("%d", count);
}